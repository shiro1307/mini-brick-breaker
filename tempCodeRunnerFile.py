def fade_in(self):
        ## fade in
        if self.fade_alpha < 255:
            self.fade_alpha += 100 * get_frame_time()
        draw_rectangle(0,0,SCREEN_W,SCREEN_H,Color(0,0,0, 255 - min(255, int(self.fade_alpha)) ))
