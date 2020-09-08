import time
from life_controller import controller


def life_game(x: int, y: int):
    lc = controller(x, y)
    lives = lc.summon_lives()
    int_generation = 0

    # 機能の備忘録用関数
    # forSystemExplain(lives)

    while True:
        int_generation += 1
        lc.checkLivesStatus(lives, int_generation)
        lives = lc.tell_around_status(lives)
        lives = lc.go2next_generation(lives)

        time.sleep(0.1)


# 機能の備忘録用関数
def forSystemExplain(lives):
    # life objectのlist(world全体)
    print(type(lives))
    # 1行目の辞書list
    print(type(lives[0]))
    # 1行目key'0'のlife object本体
    print(type(lives[0][0]))


if __name__ == '__main__':
    life_game(10, 10)
