from pyray import *
import utils
SCREEN_W,SCREEN_H = utils.SCREEN_W,utils.SCREEN_H
dtfac = 3000
import math

def clamp(value, min_val, max_val):
    return max(min_val, min(value, max_val))  

class Paddle:

    def __init__(self):
        self.w = 85
        self.h = 16
        self.x = SCREEN_W/2
        self.y = SCREEN_H - 50
        self.speed = 0.1
        self.ball = None
        self.sprite1 = load_texture("art/paddlenew.png")
        self.sprite2 = load_texture("art/paddlepush2.png")
        set_texture_filter(self.sprite1, TextureFilter.TEXTURE_FILTER_POINT)
        set_texture_filter(self.sprite2, TextureFilter.TEXTURE_FILTER_POINT)
    
    def draw(self):
        #draw_rectangle_lines( math.floor(self.x - self.w/2) ,  math.floor(self.y) , self.w , self.h , WHITE)

        bdis = vector2_distance( Vector2(self.x,self.y) , Vector2(self.ball.x,self.ball.y) )
        sp = self.sprite1

        if bdis <= self.ball.r + 30:
            sp = self.sprite2

        draw_texture_pro(
            sp,
            Rectangle(0,0,sp.width,sp.height),
            Rectangle(self.x-self.w/2,self.y,self.w,self.h),
            Vector2(0,0),
            0,
            WHITE
        )

    def update(self):
        self.handle_control()

    def handle_control(self):

        dt = get_frame_time()* dtfac

        if is_key_down(KeyboardKey.KEY_SPACE):
            if self.ball and self.ball.stuck:
                self.ball.stuck = False #unstick ball

        if is_key_down(KeyboardKey.KEY_LEFT) and not is_key_down(KeyboardKey.KEY_RIGHT):
            self.x -= self.speed * dt
        elif is_key_down(KeyboardKey.KEY_RIGHT) and not is_key_down(KeyboardKey.KEY_LEFT):
            self.x += self.speed * dt
        
        self.x = clamp(self.x,self.w/2,SCREEN_W-self.w/2)
