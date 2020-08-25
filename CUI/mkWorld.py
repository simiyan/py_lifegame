import os, time, sys
from life_controller import controller

def life_game(x, y):
    lw = controller(x, y)
    lives = lw.summon_lives()
    int_generation = 0
    
    while True:
        int_generation += 1
        lw.checkLivesStatus(lives, int_generation)
        lives = lw.tell_around_status(lives)
        lives = lw.go2next_generation(lives)
        
        time.sleep(0.1)
    
if __name__=='__main__':
    life_game(10, 10)
    