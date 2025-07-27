from pyray import *
import utils

SCREEN_W,SCREEN_H = utils.SCREEN_W,utils.SCREEN_H

import random
import math

class Menu:
    def __init__(self):
        self.fade_alpha = 0
        self.splash = load_texture("art/broken tile.png")
        self.music = load_music_stream("sound/new_song.wav")
        play_music_stream(self.music)
        self.music.looping = True

    def fade_in(self):
        ## fade in
        if self.fade_alpha < 255:
            self.fade_alpha += 100 * get_frame_time()
        draw_rectangle(0,0,SCREEN_W,SCREEN_H,Color(0,0,0, 255 - min(255, int(self.fade_alpha)) ))

    def update(self):
        update_music_stream(self.music)

    def play_prompt(self):
        draw_text( "[Press SPACE to play]".center(34) ,
                  25 , int(SCREEN_H*0.9) , 40 ,
                  Color(0,0,0, int(255 * abs(math.sin(get_time()*2))) ) 
                  )
        if is_key_released(KeyboardKey.KEY_SPACE):
            utils.curr_screen = "game"

    def draw(self):

        draw_texture_pro(
            self.splash,
            Rectangle(0,0,self.splash.width,self.splash.height),
            Rectangle(0,0,SCREEN_W,SCREEN_H),
            Vector2(0,0),
            0,
            WHITE
        )

        draw_text("Mini \nBrick-Breaker",40,40,50,BLACK)
        draw_text("By Shardul H.",40,160,27,BLACK)

        self.play_prompt()

        self.fade_in()