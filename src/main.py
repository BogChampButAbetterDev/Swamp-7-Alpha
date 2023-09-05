import pygame as pg
import sys
from settings import *
from mode7 import Mode7
from setup import *
from cmd_things import *

class App:
    def __init__(self, floor_text, ceil_text) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()
        self.renderer = Mode7(self, floor_text, ceil_text)

    def update(self):
        self.renderer.update()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() : .1f}')
    
    def draw(self):
        self.renderer.draw()
        pg.display.flip()

    def check_events(self):
        for i in pg.event.get():
            if i.type == pg.QUIT or (i.type == pg.KEYDOWN and i.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001
    
    def run(self):
        while True:
            self.check_events()
            self.get_time()
            self.update()
            self.draw()

if __name__ == '__main__':
    result = cmd()
    render = result[0]
    floor_texture = result[1]
    ceiling_texture = result[2]

    if render:
        app = App(floor_texture, ceiling_texture)  # Pass the obtained textures to App constructor
        app.run()
