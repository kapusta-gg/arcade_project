import arcade
from consts import *

from PIL import Image


class Player(arcade.Sprite):
    IMAGE = Image.open(
        "source/PNG/Players/Tiles/tile_0001.png").convert("RGBA")
    SPEED = 20

    def __init__(self):
        super().__init__(arcade.Texture(self.IMAGE), 1,
                         WINDOW_SIZES[0] // 2, WINDOW_SIZES[1] // 2)
        self._setup()

    def _setup(self):
        self.velocity = 0, 0

    def update(self, delta_time: float, keys: set):
        self.velocity = Player._update_velocity(keys)
        self.center_x = self.center_x + self.change_x * delta_time
        self.center_y = self.center_y + self.change_y * delta_time

    @classmethod
    def _update_velocity(cls, keys: set) -> tuple[int, int]:
        '''
        Обновление вектора скорости игрока

        :param keys: Множество нажатых кнопок
        :type keys: set
        :return: список векторов скорости
        :rtype: tuple[int, int]
        '''
        x_vel = y_vel = 0
        x_vel -= cls.SPEED if 97 in keys else 0
        x_vel += cls.SPEED if 100 in keys else 0
        y_vel -= cls.SPEED if 115 in keys else 0
        y_vel += cls.SPEED if 119 in keys else 0
        return x_vel, y_vel
