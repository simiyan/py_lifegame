import sys
import os
import datetime
import cv2
import numpy as np
from pathlib import Path
from PySide6.QtWidgets import QApplication, QWidget

sys.path.append(str(Path(__file__).resolve().parent.parent))

from PySide6 import QtGui as gui, QtCore
from CUI.life_controller import controller

from pictbox import Ui_Dialog
from QLabel_Clickable import QLabel_Clickable


BASE_DIR = Path(__file__).resolve().parent.parent
RESOURCE_DIR = BASE_DIR / "resources"


class world_ui(QWidget):
    # resource名を指定
    static_label_name = "imgLabel"
    static_generation = "世代"
    static_buffer_ten = 10
    static_logdir_name = "my_life_diary"
    static_video_sizex = 500
    static_video_sizey = 635

    static_alive_pict = 'maru25.png'
    static_dead_pict = 'batsu25.png'

    static_pict_size = 25

    # constractor:label, paramater, buttonの機能をdefine
    def __init__(self, worldx, worldy, parent=None):
        super(world_ui, self).__init__(parent)
        self.nowtime = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        self.worldx, self.worldy = worldx, worldy

        # resource_pathの定義：pict_path
        # self.static_alive_pict_path = self.resource_path(self.static_alive_pict)
        # self.static_dead_pict_path = self.resource_path(self.static_dead_pict)

        # # 世界の大きさはクラス変数で所持
        # self.value_maxx = worldx
        # self.value_maxy = worldy

        # # labelへのアクセスキーと実態
        # self.static_label_name_list = []
        # self.dictLabel = {}

        # # 初期のpict[0][0](label)の配置path位置
        # txtStatusHight = 70
        # self.init_placex = 10
        # self.init_placey = 75 + txtStatusHight
        # self.flgContinue = False

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.resize(worldx * 25 + 100, worldy * 25 + 100)

        # ラベルの管理
        self.dictLabel = self.initUI(worldx, worldy)

        # QTimer のセットアップ
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.game_tick)
        self.timer.setInterval(100)  # 100ミリ秒ごとに更新

        # world size * pict_size + (x, y 初期値) + 10(buffer) のサイズにdialogを変更する
        worldsizex = worldx * self.static_pict_size + self.init_placex + self.static_buffer_ten
        resizex = worldsizex if worldsizex > 340 + 80 + self.static_buffer_ten else 340 + 80 + self.static_buffer_ten
        resizey = worldy * self.static_pict_size + self.init_placey + self.static_buffer_ten
        self.resize(resizex, resizey)

        # 初期化。動的に自作labelを生成する
        # その際、nameとlabelの組合せ辞書を受け取る
        self.dictLabel.update(self.initUI(self.worldx, self.worldy))
        self.size_of_world = (self.worldx, self.worldy)

        # btnWorldTick押下時に、worldサイズを渡す
        self.ui.btnWorldTick.clicked.connect(lambda: self.btnStart_clicked(self.size_of_world))
        self.ui.btnRandomSet.clicked.connect(self.btnRandomSet_clicked)
        self.ui.btnReset.clicked.connect(self.btnReset_clicked)
        self.ui.btnStopPause.clicked.connect(self.btnStopPause_clicked)
        self.ui.cmbInitialData.currentIndexChanged.connect(self.cmbChanged)

        self.ui.cmbInitialData.addItem("a")
        self.ui.cmbInitialData.addItem("b")
        # selectedindexを変える
        self.ui.cmbInitialData.setCurrentIndex(1)
        # selectedindexを取得する
        #  print(self.ui.cmbInitialData.currentIndex())
        # 選択中のitemの値を取得する
        # print(self.ui.cmbInitialData.itemText(self.ui.cmbInitialData.currentIndex()))

        # # *** for pict save directory/will change to function ***
        # if not os.path.exists(self.static_logdir_name):
        #     os.mkdir(self.static_logdir_name)
        # フラグ管理
        self.running = False
        self.int_generation = 0
        self.lw = None
        self.lives = None

        # 画像保存ディレクトリ作成
        self.capturedir = os.path.join("my_life_diary", self.nowtime)
        os.mkdir(self.capturedir)

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

    # 初期化：labelを規定数配置し、その情報を返却
    def initUI(self, worldx, worldy):
        result = {}
        for y in range(worldy):
            self.init_placex = 10
            for x in range(worldx):
                labelName = self.static_label_name + str(x) + "_" + str(y)

                # labelをworldの回数定義し、nameとobjectを辞書で返却
                result.update(self.mkLabel(self.init_placex, self.init_placey, labelName))

                self.static_label_name_list.append(labelName)
                self.init_placex += self.static_pict_size
            self.init_placey += self.static_pict_size
        return result

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

    # labelの変更後status listを参照し、各labelのstatusを変更する
    # 仮引数ではアドレスが変わってしまうため、インスタンス変数を直接編集し、returnはしない
    def labels_chg_status(self, status_list: list):
        for s in range(len(status_list)):
            for r in range(len(status_list[s])):
                label_name = self.static_label_name + str(r) + "_" + str(s)
                if status_list[s][r] == 0:
                    img = gui.QImage(self.static_dead_pict_path)
                    self.dictLabel[label_name].change_status(0)

                elif status_list[s][r] == 1:
                    img = gui.QImage(self.static_alive_pict_path)
                    self.dictLabel[label_name].change_status(1)

                self.dictLabel[label_name].setPixmap(gui.QPixmap.fromImage(img))

    # 与えられたstatusによって、画像とstatusを反転させる
    def label_reverse_status(self, status, imglbl: QLabel_Clickable):
        if status == 0:
            img = gui.QImage(self.static_alive_pict_path)
            imglbl.change_status(1)

        elif status == 1:
            img = gui.QImage(self.static_dead_pict_path)
            imglbl.change_status(0)

        imglbl.setPixmap(gui.QPixmap.fromImage(img))

    # ラベルクリック時にstatusによって画像を変更する
    def lbl_clicked(self, imglbl: QLabel_Clickable):
        status = imglbl.tell_status()
        self.label_reverse_status(status, imglbl)

        reason = (imglbl.tell_status(), "manual")
        self.txtStatusUpdate(imglbl.tell_myname(), reason)

    # 初期値をlivesに与えるための、labelのstatusを集める。
    def collect_labels_status(self, init_world):
        result1st = []
        # lblのstatusをつめたリストを作成
        for name in self.static_label_name_list:
            result1st.append(self.dictLabel[name].tell_status())

        result2nd = np.array(result1st).reshape(init_world[1], -1).tolist()
        return result2nd

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

    # def btnStopPause_clicked(self):
    #     if self.flgContinue is True:
    #         self.flgContinue = False

    #     elif self.flgContinue is False:
    #         self.flgContinue = True
    def btnStopPause_clicked(self):
        """ 停止・再開ボタン """
        if self.running:
            self.running = False
            self.timer.stop()
        else:
            self.running = True
            self.timer.start()

    # make video from screenshot
    def save_video(self):
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

    # # loopをstopする/labelのstatusをクリアする/status boxをクリアする
    # def btnReset_clicked(self):
    #     # name listの名前を持つ各labelのstatusを0に変更する
    #     for name in self.static_label_name_list:
    #         self.dictLabel[name].change_status(0)

    #     # labelのstatusリストを入手する
    #     zero_label = self.collect_labels_status(self.size_of_world)

    #     # 画像の変更をする
    #     self.labels_chg_status(zero_label)

    #     self.save_video()
    #     self.ui.txtLifeStatus.setText("")
    #     self.ui.lblGeneration.setText(self.static_generation)
    def btnReset_clicked(self):
        """ リセットボタン """
        self.running = False
        self.timer.stop()
        self.int_generation = 0
        self.clear_board()  # 盤面をクリアする関数（必要に応じて実装）

    # randomボタンクリック時randomに値をsetする
    def btnRandomSet_clicked(self):
        # statusをrandomにsetさせる
        for name in self.static_label_name_list:
            self.dictLabel[name].change_status_random()
        random_label = self.collect_labels_status(self.size_of_world)
        self.labels_chg_status(random_label)

    # worldNoをinclimentする
    def updateWorldNo(self):
        world_no = self.ui.lblWorldNo.text()
        int_world_no = int(world_no) + 1
        self.ui.lblWorldNo.setText(str(int_world_no))

    # ボタンクリック時にlife_gameをstartする
    # def btnStart_clicked(self, init_world):
    #     int_generation = 0
    #     self.flgContinue = True
    #     self.updateWorldNo()

    #     # lblのstatusをつめたリストを作成
    #     label_status_list = self.collect_labels_status(init_world)
    #     # worldを生成する
    #     lw = controller(init_world[0], init_world[1])

    #     # ------------life_game_start ------------ #
    #     # labelから得たlivesの初期値を渡す #
    #     lives = lw.summon_lives("manual", label_status_list)

    #     # flgの監視 > life_game
    #     while True:
    #         QApplication.processEvents()
    #         while self.flgContinue:
    #             int_generation += 1
    #             self.ui.lblGeneration.setText(str(int_generation) + self.static_generation)

    #             # cui出力
    #             # lw.checkLivesStatus(lives, int_generation)

    #             # 各livesの周辺を調査し、次のstatusを教える
    #             lives = lw.tell_around_status(lives)

    #             # life_statusをlabel_statusに反映
    #             label_status_list = lw.collect_lives_status(lives)

    #             # labels_statusによりstatusと画像を更新する
    #             self.labels_chg_status(label_status_list)

    #             # lifeとGUIの更新
    #             QApplication.processEvents()
    #             lives = lw.go2next_generation(lives)

    #             # タイムラグをおく
    #             # time.sleep(1)
    #             # 世代ごとに画像保存：3桁.jpg
    #             capture_name = self.capturedir + "/" + str('{0:03d}.jpg'.format(int_generation))
    #             self.grab().save(capture_name)

    def btnStart_clicked(self, init_world):
        """ スタートボタンクリック時にライフゲーム開始 """
        if not self.running:
            self.running = True
            self.int_generation = 0
            self.updateWorldNo()

            # lblのstatusをつめたリストを作成
            label_status_list = self.collect_labels_status(init_world)

            # worldを生成する
            self.lw = controller(init_world[0], init_world[1])

            # labelから得たlivesの初期値を渡す
            self.lives = self.lw.summon_lives("manual", label_status_list)

            self.timer.start()

    # convert to resource path, return:path of resource
    def resource_path(self, relative_path):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, relative_path)
        return str(RESOURCE_DIR / relative_path)

    def clear_board(self):
        """ 盤面をリセットし、すべてのセルを初期状態に戻す """
        for label in self.dictLabel.values():
            label.setPixmap(gui.QPixmap("resources/batsu25.png"))  # 死の状態の画像を設定
        self.ui.lblGeneration.setText("0" + self.static_generation)  # 世代数をリセット


# 単体call時の動作
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = world_ui(20, 20)
    window.show()
    sys.exit(app.exec())
