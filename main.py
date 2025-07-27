from pyray import *
import utils
SCREEN_W,SCREEN_H = utils.SCREEN_W,utils.SCREEN_H

from game import Game
from menu import Menu
import math

init_window(SCREEN_W,SCREEN_H, "mini-brick-breaker")
init_audio_device()
set_target_fps(60)

game = Game()
                
menu = Menu()

while not window_should_close():

    clear_background(WHITE)

    if utils.curr_screen == "game":
        game.update()
        begin_drawing()
        game.draw()
        end_drawing()
    
    if utils.curr_screen == "menu":
        menu.update()
        begin_drawing()
        menu.draw()
        end_drawing()

close_window()