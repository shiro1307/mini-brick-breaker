from pyray import *
import utils
SCREEN_W,SCREEN_H = utils.SCREEN_W,utils.SCREEN_H
import math

dtfac = 3000

class Ball:
    def __init__(self):
        self.brick_array = None
        self.paddle = None
        self.x = 30
        self.y = 30
        self.r = 10
        self.speed = 0.09
        self.vx = self.speed
        self.vy = -self.speed
        self.stuck = True
        self.game = None
        self.sprite = load_texture("art/balll.png")

        self.bounce_sound = load_sound("sound/laserShoot.wav")
        self.pop_sound = load_sound("sound/pop.wav")
        self.brick_sound = load_sound("sound/explosion.wav")

        set_texture_filter(self.sprite, TextureFilter.TEXTURE_FILTER_POINT)
    
    def collide_with_walls(self):

        if self.x <= self.r:
            self.x = self.r + 1
            self.vx *= -1
            play_sound(self.bounce_sound)
        elif self.x >= SCREEN_W-self.r:
            self.x = SCREEN_W-self.r - 1
            self.vx *= -1
            play_sound(self.bounce_sound)
        elif self.y <= self.r:
            self.y = self.r + 1
            self.vy *= -1
            play_sound(self.bounce_sound)
    
    def collide_with_paddle(self):

        if self.paddle:

            p = self.paddle

            iscoll = (self.x >=p.x-p.w/2 and self.x <=p.x+p.w/2) and (self.y+self.r>=p.y and self.y-self.r<=p.y+p.h)

            if iscoll:

                play_sound(self.bounce_sound)
                play_sound(self.pop_sound)

                offset = (self.x - p.x)/(p.w/2)
                angle = (math.pi/3) * offset
                self.vx = self.speed * math.sin(angle) * 1.5
                self.vy = -self.speed * math.cos(angle) * 1.5

    def collide_with_brick(self, b):
        
        iscoll = check_collision_circle_rec(Vector2(self.x,self.y), self.r, Rectangle(b.x,b.y,b.w,b.h) )

        if b and b.hp >0 and iscoll:

            play_sound(self.brick_sound)

            dx = self.x - (b.x + b.w/2)
            dy = self.y - (b.y + b.h/2)

            ph = b.w/b.h

            if abs(dx)/abs(dy) >= ph:
                self.vx *= -1
            else:
                self.vy *= -1

            b.hp -= 1

            if b.hp == 0:
                self.game.score += 1

    def check_collision_all_bricks(self):
        
        for i in self.brick_array[:]:

            if i.hp > 0:
                self.collide_with_brick(i)

    def destroy_dead_bricks(self):
        
        for i in self.brick_array[:]:

            if i.hp == -1:
                self.brick_array.remove(i)

    def move(self):
        if not self.stuck:
            dt = get_frame_time()* dtfac
            self.x += self.vx * dt
            self.y += self.vy * dt

    def attach_to_paddle(self):
        if self.stuck and self.paddle:
            self.x = math.floor(self.paddle.x)
            self.y = math.floor(self.paddle.y-self.r-1)

    def update(self):
        self.attach_to_paddle()
        self.move()
        self.collide_with_walls()
        self.collide_with_paddle()
        self.destroy_dead_bricks()
        self.check_collision_all_bricks()

    def draw(self):

        #draw_circle(math.floor(self.x),math.floor(self.y),math.floor(self.r),RED)

        draw_texture_pro(
            self.sprite,
            Rectangle(0,0,self.sprite.width,self.sprite.height),
            Rectangle(self.x-self.r,self.y-self.r,2*self.r,2*self.r),
            Vector2(0,0),
            0,
            WHITE
        )
