import os
from lives import life
# livesをsummonし、observeし、next_generationに交代させる


class controller:
    world_x = 0
    world_y = 0

    def __init__(self, maxX, maxY):
        # (JP)世界の大きさ
        # (ENG)Size of World
        self.world_x = maxX
        self.world_y = maxY

        # (JP)worldの南北を示す配列
        # (ENG)Array for North South
        self.field_of_lives_row = []

    # livesをsummonし、worldを返却
    def summon_lives(self):
        #
        #
        #
        #
        #
        # worldの行を示す配列に辞書を入れる。
        # cは南北方向にsummonする回数を表す。
        # また、lifeオブジェクトに初期の位置情報(y)を提供する。
        for c in range(self.world_y):
            # worldの東西を示す辞書(セルの列数)
            # 次の行にメンバーを追加する前にリセットする
            field_of_lives_column = {}
            # worldの列を示す辞書に、lifeオブジェクトを入れる
            # 辞書のkeyはそのままlifeのid(識別子)となる
            for i in range(0, self.world_x, 1):
                # c行 i列に座標(c,i)を初期値とするlifeをsummon
                # 将来的にmanual modeを実装したい(未対応)。今は"auto"で自動設定
                field_of_lives_column[i] = life(c, i, "auto")

            # 列のメンバー辞書を行の位置配列に保存する
            self.field_of_lives_row.append(field_of_lives_column)
        return self.field_of_lives_row

    # 各livesの周辺を調査し、周辺の合計値を各lifeオブジェクトに伝える
    def tell_around_status(self, lives):
        # worldを見回る
        for i in range(len(lives)):
            for livesID, objLives in lives[i].items():
                # 1.targetのlifeの位置情報を取得する
                life_place = objLives.tell_place()

                # 2.得られた位置情報から周辺座標を計算する
                around_places = self.calc_around_places(life_place)

                # 3.周辺座標のlifeにstatusを聞き、合計する。その際、自己情報は除外する
                sum_status = self.hear_status(around_places, lives, life_place)

                # 4.targetのlifeに周辺の合計を教える
                # 将来的にstatusの変更理由も表示させたい(未対応)。そのための変数.
                # 一時的にコメントアウト
                ### change_result = objLives.change_status(sum_status)

        return lives

    # 2.得られた位置情報から周辺座標を計算する。
    def calc_around_places(self, myplace):
        # 周辺調査用ループ数
        minus_one = -1
        zero = 0
        plus_one = 1
        plus_two = 2

        # 結果：タプルリスト
        result = []
        # 自己位置から、周辺座標を計算し、tupple listに格納する
        for i in range(minus_one, plus_two, plus_one):
            for j in range(minus_one, plus_two, plus_one):
                place = (myplace[zero] + i, myplace[plus_one] + j)
                result.append(place)
        return result

    # 3.周辺座標のlifeにstatusを聞き、合計する。その際、自己情報は除外する
    def hear_status(self, places, lives, myplace):
        result = 0
        for place in places:
            targetx = place[1]
            targety = place[0]
            # 行座標がマイナスの場合、有効範囲外とし、0加算とする
            if targety < 0:
                result += 0
            elif myplace == place:
                pass
            else:
                try:
                    result += lives[targety][targetx].tell_status()
                except (KeyError, IndexError):
                    result += 0

        return result

    # current_statusをnext_statusに書き換えさせる
    def go2next_generation(self, lives):
        # worldを見回って世代交代を指示
        for i in range(len(lives)):
            for livesID, objLives in lives[i].items():
                objLives.my_life_tick()

        return lives

    # livesのstatusをoutputする
    def checkLivesStatus(self, target, generation):
        OS_WIN = 'nt'
        OS_UNIX = 'posix'
        if os.name == OS_WIN:
            os.system('cls')
            
        elif os.name == OS_UNIX:
            os.system('clear')
            
        print(str(generation) + "世代")
        for i in range(len(target)):
            for livesID, objLives in target[i].items():
                print(objLives.tell_status(), end="")
            print()
