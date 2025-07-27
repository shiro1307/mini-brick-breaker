from pyray import *
import utils
SCREEN_W,SCREEN_H = utils.SCREEN_W,utils.SCREEN_H
import math
import random

dtfac = 3000

class Brick:
    def __init__(self,brick_array,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = 1
        self.brick_array = brick_array
        self.animate_timer = 0
        self.animate_length = 10
        brick_array.append(self)

        self.sprite = load_texture("art/purplbrick.png")
        set_texture_filter(self.sprite, TextureFilter.TEXTURE_FILTER_POINT)
        self.frames = 10
    
    def destruct(self):
        dt = get_frame_time()* dtfac
        self.animate_timer += 0.005*dt

        if self.animate_timer >= self.animate_length:
            self.hp = -1

    def update(self):
        if self.hp == 0:
            self.destruct()

    def draw(self):

        if self.hp >0:
            #draw_rectangle(self.x,self.y,self.w,self.h,BLUE)

            draw_texture_pro(
                self.sprite,
                Rectangle(0,0,72,32),
                Rectangle(self.x,self.y,self.w,self.h),
                Vector2(0,0),
                0,
                WHITE
            )

        elif self.hp == 0:
            c = self.animate_timer/self.animate_length

            frame_off_x = math.ceil(c*(self.frames-1))

            p = math.floor(c*10)

            draw_texture_pro(
                self.sprite,
                Rectangle(frame_off_x*72 ,0,72,32),
                Rectangle(self.x-p,self.y-p+c*40,self.w+2*p,self.h+2*p),
                Vector2(0,0),
                0,
                WHITE
            )