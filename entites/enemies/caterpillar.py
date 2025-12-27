import arcade
import numpy as np

from consts import *
from entites.enemies.enemy_interface import EnemyInterface


class Caterpillar(EnemyInterface):
    IMAGE_PATH_WALK = ["source/PNG/Enemies/Tiles/tile_0000.png",
                       "source/PNG/Enemies/Tiles/tile_0001.png", "source/PNG/Enemies/Tiles/tile_0002.png"]
    SPEED = 40
    TIMER_WALK_ANIM = 0.1

    def _setup(self):
        self.velocity = 0, 0
        self.walk_timer = 0
        self.cur_anim = 0
        self.rigth_walk = True

    def update(self, delta_time: float, keys: set):
        self.chase_player()
        if self.velocity[X] < 0:
            self.rigth_walk = False
        else:
            self.rigth_walk = True
        if self.velocity[X] != 0 or self.velocity[Y] != 0:
            self.walk_timer += delta_time
            if self.walk_timer >= self.TIMER_WALK_ANIM:
                self.cur_anim = (self.cur_anim + 1) % len(self.textures_walk)
                self.walk_timer = 0
            text = self.textures_walk[self.cur_anim]
        else:
            text = self.texture_state

        if not self.rigth_walk:
            text = text.flip_left_right()
        self.texture = text

        self.center_x = self.center_x + self.change_x * delta_time
        self.center_y = self.center_y + self.change_y * delta_time
