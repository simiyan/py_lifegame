import os, time, sys
from pathlib import Path
from life_controller import controller
from PyQt5.QtWidgets import QApplication
from pictui_call import world_ui

def life_game(x, y):
    lw = controller(x, y)
    lives = lw.summon_lives("auto")
    int_generation = 0
    
    while True:
        int_generation += 1
        lw.checkLivesStatus(lives, int_generation)
        lives = lw.tell_around_status(lives)
        lives = lw.go2next_generation(lives)
        
        time.sleep(0.1)
def life_gui(x, y):
    app = QApplication(sys.argv)
    window = world_ui(x, y)
    window.show()
    sys.exit(app.exec_())
    
if __name__=='__main__':
    life_game(10, 10)
    # worldx = 4
    # worldy = 4
    # life_gui(worldx, worldy)
    