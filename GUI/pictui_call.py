import sys
import os
import datetime
import cv2
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget

sys.path.append(str(Path(__file__).resolve().parent.parent))

from PySide6 import QtGui as gui, QtCore
from CUI.life_controller import controller

from pictbox import Ui_Dialog
from QLabel_Clickable import QLabel_Clickable


BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCE_DIR = BASE_DIR / "resources"


class WorldUI(QWidget):
    # resource名を指定
    static_label_name = "imgLabel"
    static_generation = "世代"
    static_buffer_ten = 10
    static_logdir_name = "my_life_diary"
    static_video_sizex = 500
    static_video_sizey = 635
    static_pict_size = 25
    static_alive_pict = RESOURCE_DIR / "maru25.png"
    static_dead_pict = RESOURCE_DIR / "batsu25.png"

    # constractor:label, paramater, buttonの機能をdefine
    def __init__(self, worldx, worldy, parent=None):
        super(WorldUI, self).__init__(parent)
        self.nowtime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.worldx, self.worldy = worldx, worldy
        # フラグ管理
        self.running = False
        self.int_generation = 0
        self.lw = None
        self.lives = None
        self.dictLabel = {}
        self.size_of_world = (self.worldx, self.worldy)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.adjust_window_size()

        self.initUI()
        self.setupConnections()

        # QTimer のセットアップ
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.game_tick)
        self.timer.setInterval(100)  # 100ミリ秒ごとに更新

        # 画像保存ディレクトリ作成
        self.capturedir = Path(self.static_logdir_name) / self.nowtime
        self.capturedir.mkdir(parents=True, exist_ok=True)

    def adjust_window_size(self):
        txtStatusHeight = 70
        self.init_placex = 10
        self.init_placey = 75 + txtStatusHeight

        worldsizex = self.worldx * self.static_pict_size + self.init_placex + self.static_buffer_ten
        resizex = max(worldsizex, 340 + 80 + self.static_buffer_ten)

        resizey = self.worldy * self.static_pict_size + self.init_placey + self.static_buffer_ten
        self.resize(resizex, resizey)

    def initUI(self):
        for y in range(self.worldy):
            for x in range(self.worldx):
                label_name = f"{self.static_label_name}{x}_{y}"
                label = QLabel_Clickable(self)
                label.setPixmap(gui.QPixmap(str(self.static_dead_pict)))
                label.setGeometry(QtCore.QRect(x * self.static_pict_size + 10, y * self.static_pict_size + 85 + 50, self.static_pict_size, self.static_pict_size))
                label.clicked.connect(lambda lbl=label: self.lbl_clicked(lbl))
                self.dictLabel[label_name] = label

    def setupConnections(self):
        # btnWorldTick押下時に、worldサイズを渡す
        self.ui.btnWorldTick.clicked.connect(lambda: self.btnStart_clicked(self.size_of_world))
        self.ui.btnRandomSet.clicked.connect(self.btnRandomSet_clicked)
        self.ui.btnReset.clicked.connect(self.btnReset_clicked)
        self.ui.btnStopPause.clicked.connect(self.btnStopPause_clicked)
        self.ui.cmbInitialData.currentIndexChanged.connect(self.cmbChanged)
        self.ui.cmbInitialData.addItems(["a", "b"])
        self.ui.cmbInitialData.setCurrentIndex(1)

        print(self.ui.cmbInitialData.currentIndex())
        print(self.ui.cmbInitialData.itemText(self.ui.cmbInitialData.currentIndex()))

    def cmbChanged(self):
        pass
        # print("changed")

    def txtStatusUpdate(self, name, reason: tuple):
        # ex:label1はmanualにより*になった
        # reasonはstatus, reasonをもつ
        status = ""
        if reason[0] == 0:
            status = "死"

        elif reason[0] == 1:
            status = "生"

        self.ui.txtLifeStatus.append(name + "は" + reason[1] + "により" + status + "になった。")

    # (x, y)に objNameの名前をつけたimgLabelを置く(1個)。key, value:objName, Labelの組合せを返す
    def mkLabel(self, x, y, objName):
        result = {}
        image = gui.QImage(self.static_dead_pict_path)
        imageLabel = QLabel_Clickable(self)
        imageLabel.setPixmap(gui.QPixmap.fromImage(image))
        # なんのためにobjectNameをsetするのか不明。access方法も不明
        imageLabel.setObjectName(objName)
        # ObjectNameにAccessできないので自作
        imageLabel.give_myname(objName)

        imageLabel.setGeometry(QtCore.QRect(x, y, self.static_pict_size, self.static_pict_size))
        imageLabel.clicked.connect(lambda: self.lbl_clicked(imageLabel))
        result = {imageLabel.tell_myname(): imageLabel}
        return result

    def labels_chg_status(self, status_list: list):
        """ ラベルの状態を更新する """
        for y, row in enumerate(status_list):
            for x, status in enumerate(row):
                label_name = f"{self.static_label_name}{x}_{y}"
                img_path = self.static_alive_pict if status == 1 else self.static_dead_pict
                self.dictLabel[label_name].setPixmap(gui.QPixmap(str(img_path)))

    def label_reverse_status(self, status, imglbl: QLabel_Clickable):
        """ 与えられたstatusによって、画像とstatusを反転させる """
        new_status = 1 if status == 0 else 0
        img_path = self.static_alive_pict if new_status == 1 else self.static_dead_pict
        imglbl.change_status(new_status)
        imglbl.setPixmap(gui.QPixmap(str(img_path)))

    # ラベルクリック時にstatusによって画像を変更する
    def lbl_clicked(self, imglbl: QLabel_Clickable):
        status = imglbl.tell_status()
        self.label_reverse_status(status, imglbl)

        reason = (imglbl.tell_status(), "manual")
        self.txtStatusUpdate(imglbl.tell_myname(), reason)

    def collect_labels_status(self, init_world):
        """ すべてのラベルの状態を取得し、リスト化する """
        status_list = []
        for y in range(init_world[1]):
            row = []
            for x in range(init_world[0]):
                label_name = f"{self.static_label_name}{x}_{y}"
                row.append(self.dictLabel[label_name].tell_status())
            status_list.append(row)
        return status_list

    def game_tick(self):
        """ 1ターンの処理（`while True` の代替）"""
        if not self.running:
            return

        self.int_generation += 1
        self.ui.lblGeneration.setText(str(self.int_generation) + self.static_generation)

        # 各livesの周辺を調査し、次のstatusを教える
        self.lives = self.lw.tell_around_status(self.lives)

        # life_statusをlabel_statusに反映
        label_status_list = self.lw.collect_lives_status(self.lives)

        # labels_statusによりstatusと画像を更新する
        self.labels_chg_status(label_status_list)

        # 次の世代へ
        self.lives = self.lw.go2next_generation(self.lives)

        # 世代ごとに画像保存
        capture_name = os.path.join(self.capturedir, f"{self.int_generation:03d}.jpg")
        self.grab().save(capture_name)

    def btnStopPause_clicked(self):
        """ 停止・再開ボタン """
        if self.running:
            self.running = False
            self.timer.stop()
        else:
            self.running = True
            self.timer.start()

    def save_video(self):
        """ キャプチャ画像を動画として保存（進行状況をGUIに表示） """
        static_world_no = "world_no_"
        world_no = self.ui.lblWorldNo.text()
        video_name = f"{static_world_no}{world_no}.mp4"
        video_path = str(self.capturedir / video_name)  # Pathオブジェクトをstrに変換

        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        video = cv2.VideoWriter(video_path, fourcc, 90.0, (self.static_video_sizex, self.static_video_sizey))

        images = sorted(self.capturedir.glob("*.jpg"))
        now_generation = len(images)  # 画像の総数から世代数を取得

        for i, img_path in enumerate(images, start=1):
            QApplication.processEvents()
            img = cv2.imread(str(img_path))
            if img is None:
                continue
            img = cv2.resize(img, (self.static_video_sizex, self.static_video_sizey))

            # 各フレームを複数回書き込んでフレームレートを調整
            for _ in range(25):
                video.write(img)

            # 進捗をGUIに表示
            self.ui.txtLifeStatus.append(f"{i}/{now_generation} is processed.")

            if self.ui.chkRemovePict.isChecked():
                img_path.unlink()
        video.release()
        self.ui.txtLifeStatus.clear()

    # make video from screenshot
    def save_video_old(self):
        static_world_no = "world_no_"
        world_no = self.ui.lblWorldNo.text()
        video_name = static_world_no + world_no + ".mp4"

        fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
        video = cv2.VideoWriter(self.capturedir + "/" + video_name, fourcc, 90.0, (self.static_video_sizex, self.static_video_sizey))

        now_generation = self.ui.lblGeneration.text()[:-1]
        now_generation = now_generation[:-1]

        for i in range(1, int(now_generation) + 1):
            QApplication.processEvents()
            pictpath = self.capturedir + "/" + '{0:03d}.jpg'.format(i)
            img = cv2.imread(pictpath)
            img = cv2.resize(img, (self.static_video_sizex, self.static_video_sizey))

            # 同じ画像を複数回表示することで1画像の表示時間を長くする
            for double_times in range(1, 25):
                video.write(img)

            if self.ui.chkRemovePict.isChecked():
                os.remove(pictpath)
            self.ui.txtLifeStatus.append(str(i) + "/" + now_generation + " is processed.")
        video.release()

    def btnReset_clicked(self):
        """ リセットボタン：ゲーム状態を初期化 """
        self.running = False
        self.timer.stop()
        self.int_generation = 0
        self.clear_board()
        self.ui.txtLifeStatus.setText("")  # テキストボックスをクリア
        self.save_video()  # 世代ごとの画像保存

    # randomボタンクリック時randomに値をsetする
    def btnRandomSet_clicked(self):
        """ 全てのセルの状態をランダムに変更 """
        for name in self.dictLabel:  # self.static_label_name_list ではなく self.dictLabel を使う
            self.dictLabel[name].change_status_random()

        random_label = self.collect_labels_status(self.size_of_world)
        self.labels_chg_status(random_label)

    # worldNoをinclimentする
    def updateWorldNo(self):
        world_no = self.ui.lblWorldNo.text()
        int_world_no = int(world_no) + 1
        self.ui.lblWorldNo.setText(str(int_world_no))

    def btnStart_clicked(self, init_world):
        if not self.running:
            self.running = True
            self.int_generation = 0
            self.updateWorldNo()

            # 盤面の初期状態を取得
            label_status_list = self.collect_labels_status(init_world)

            # コントローラーを生成し、ライフゲームを開始
            self.lw = controller(init_world[0], init_world[1])
            self.lives = self.lw.summon_lives("manual", label_status_list)

            # **初期盤面を UI に反映**
            self.labels_chg_status(label_status_list)

            # **最初のゲームステップを強制実行**
            self.game_tick()

            # **タイマーを開始**
            self.timer.start()

    # convert to resource path, return:path of resource
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return str(Path(sys._MEIPASS) / relative_path)
        return str(RESOURCE_DIR / relative_path)

    def clear_board(self):
        """ 盤面をリセットし、すべてのセルを初期状態に戻す """
        for label in self.dictLabel.values():
            label.setPixmap(gui.QPixmap(self.static_dead_pict))  # 死の状態の画像を設定
        self.ui.lblGeneration.setText("0" + self.static_generation)  # 世代数をリセット


# 単体call時の動作
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WorldUI(20, 20)
    window.show()
    sys.exit(app.exec())
