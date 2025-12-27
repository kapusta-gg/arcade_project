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
        self.camera = arcade.Camera2D()
        self.camera.width = CAMERA_WIDTH
        self.camera.height = CAMERA_HEIGHT

    def setup(self):
        arcade.set_background_color(arcade.color.FERN_GREEN)
        self.player = Player()
        self.sprites.append(self.player)

        self.map = arcade.load_tilemap("./maps/level1.tmx", scaling=2.5)
        self.scene = arcade.Scene.from_tilemap(self.map)

        self._create_enemies(1)

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.sprites.draw()
        self.camera.use()

    def on_update(self, delta_time):
        self.sprites.update(delta_time, self.keys)

        pos = (self.player.center_x, self.player.center_y)
        self.camera.position = arcade.math.lerp_2d(
            self.camera.position,
            pos,
            CAMERA_LERP,
        )

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
