import arcade
from consts import *
from entites.player import Player
from entites.enemies.enemies import *


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.sprites = arcade.SpriteList()
        self.enemis = arcade.SpriteList()
        self.keys = set()

    def setup(self):
        arcade.set_background_color(arcade.color.FERN_GREEN)
        self.player = Player()
        self.sprites.append(self.player)

        self._create_enemies(1)

    def on_draw(self):
        self.clear()
        self.sprites.draw()

    def on_update(self, delta_time):
        self.sprites.update(delta_time, self.keys)

    def on_key_press(self, symbol, modifiers):
        self.keys.add(symbol)

    def on_key_release(self, symbol, modifiers):
        self.keys.remove(symbol)

    def _create_enemies(self, n: int) -> None:
        WINDOW_SIZES = get_settings("window_sizes")
        for _ in range(n):
            x, y = arcade.math.rand_in_rect(arcade.rect.XYWH(
                WINDOW_SIZES[X] // 2, WINDOW_SIZES[Y] // 2,
                WINDOW_SIZES[X] - PIXELS_BOARD, WINDOW_SIZES[Y] - PIXELS_BOARD))
            enemy = Rabbit(x, y, self.player)
            self.sprites.append(enemy)
            self.enemis.append(enemy)
