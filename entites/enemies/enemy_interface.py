import arcade
import numpy as np


class EnemyInterface(arcade.Sprite):
    IMAGE_PATH_WALK = ...
    SPEED = ...
    TIMER_WALK_ANIM = ...

    def __init__(self, x, y, player: arcade.Sprite):
        super().__init__(center_x=x, center_y=y, scale=2)
        self._setup()
        self.textures_walk = [arcade.load_texture(
            text) for text in self.IMAGE_PATH_WALK]
        self.texture_state = self.textures_walk[0]
        self.texture = self.texture_state

        self.player = player

    def _setup(self):
        ...

    def death(self):
        ...

    def attack(self):
        ...

    def chase_player(self):
        sign_x = np.sign(self.player.center_x - self.center_x)
        sign_y = np.sign(self.player.center_y - self.center_y)
        self.velocity = (sign_x * self.SPEED, sign_y * self.SPEED)
