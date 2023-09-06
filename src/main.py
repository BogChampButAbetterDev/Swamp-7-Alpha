import pygame as pg
from mode7 import Mode7 
import sys
from settings import *
from cmd_things import *

class App:
    def __init__(self, floor_text, ceil_text) -> None:
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

        # Initialize delta to a default value
        self.dt = 0.0

        # Create an instance of the Mode 7 class and pass the delta value
        self.renderer = Mode7(self, floor_text, ceil_text, self.dt)

    def update(self):
        self.dt = self.calculate_delta_time()  # Calculate delta time before updating
        self.renderer.delta = self.dt  # Update the Mode 7 instance with the new delta value
        self.renderer.update()
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
    
    def calculate_delta_time(self):
        dt = self.clock.tick(FPS) / 1000.0 
        return dt
    
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
        app = App(floor_texture, ceiling_texture)
        app.run()
