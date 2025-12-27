import arcade
import numpy as np


class EnemyInterface:
    IMAGE_PATH_WALK = ...
    SPEED = ...
    TIMER_WALK_ANIM = ...

    def __init__(self, player: arcade.Sprite):
        self.player = player

    def death(self):
        ...

    def attack(self):
        ...

    def chase_player(self):
        sign_x = np.sign(self.player.center_x - self.center_x)
        sign_y = np.sign(self.player.center_y - self.center_y)
        self.velocity = (sign_x * self.SPEED, sign_y * self.SPEED)
