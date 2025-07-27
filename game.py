from pyray import *
import utils
SCREEN_W,SCREEN_H = utils.SCREEN_W,utils.SCREEN_H

from paddle import Paddle
from ball import Ball
from brick import Brick
import random
import math

class Game:
    def __init__(self):
        self.all_bricks = []
        self.score = 0
        self.ball = Ball()
        self.paddle = Paddle()
        self.ball.brick_array = self.all_bricks
        self.ball.paddle = self.paddle
        self.ball.game = self
        self.paddle.ball = self.ball
        self.state = "running"
        self.fade_alpha = 0

        self.generate_bricks()
    
    def fade_in(self):
        ## fade in
        if self.fade_alpha < 255:
            self.fade_alpha += 100 * get_frame_time()
        draw_rectangle(0,0,SCREEN_W,SCREEN_H,Color(0,0,0, 255 - min(255, int(self.fade_alpha)) ))

    
    def end_scores(self):

        if self.state =="win" or self.state =="loss":

            draw_rectangle(15,15,SCREEN_W-15,120, WHITE)
            draw_rectangle_lines(15,15,SCREEN_W-30,120, BLACK)

            draw_text("Score: " + str(self.score), 30,90,30,BLACK)

            draw_text( "[Press space to continue]" , 25 , 160 , 20 , Color(0,0,0, int(255 * abs(math.sin(get_time()*2))) ) )

            if is_key_released(KeyboardKey.KEY_SPACE):
                self.__init__()
                utils.curr_screen = "menu"

            if self.state =="win":
                draw_text("Level cleared!", 30,30,40,BLACK)
                
            if self.state =="loss":
                draw_text("You lost.", 30,30,40,BLACK)


    def generate_bricks(self):

        nx = 7
        ny = 8
        rx,ry,rox,roy = SCREEN_W*0.8 ,SCREEN_H*0.4, SCREEN_W*0.1 , SCREEN_H*0.1
        pad = 3

        for x in range(nx):
            for y in range(ny):

                if random.randint(0,10) > 4:

                    brkw,brkh = rx/nx,ry/ny

                    print(brkw,brkh)

                    brkx = x*brkw +rox + pad
                    brky = y*brkh +roy + pad

                    brkw-=2*pad
                    brkh-=2*pad

                    brk = Brick(self.all_bricks, math.floor(brkx) , math.floor(brky) , math.floor(brkw), math.floor(brkh) )

    def draw_all_bricks(self):

        for i in self.all_bricks:
            i.draw()
            i.update()

    def check_win_loss(self,ball):

        if ball.y >= SCREEN_H:
            ball.vx = 0
            ball.vy = 0
            self.state = "loss"
        
        if len(self.all_bricks) == 0:
            ball.vx = 0
            ball.vy = 0
            self.state = "win"

    def show_score(self):
        thickness = 28
        draw_rectangle( 0 , math.floor(SCREEN_H - thickness) , SCREEN_W , thickness , Color(26, 26, 26,255) )
        #draw_rectangle( 0 , math.floor(SCREEN_H - thickness) + 3 , SCREEN_W , math.floor(thickness/3) , Color(54, 54, 54,255) )

        draw_text("Score: " + str(self.score) , 15 , math.floor(SCREEN_H - thickness)+5, thickness -6 ,WHITE)

    def update(self):
        if self.state == "running":
            self.check_win_loss(self.ball)
            self.paddle.handle_control()

            self.paddle.update()
            self.ball.update()

    def draw(self):

        clear_background(WHITE)

        draw_text( str(self.score) , 0 , 0 , 30 , WHITE )

        self.draw_all_bricks()
        self.paddle.draw()
        self.ball.draw()

        self.show_score()
        self.end_scores()

        self.fade_in()
