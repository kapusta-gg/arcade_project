import arcade
from entites.player import Player
from consts import *


class MainWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)
        self.sprites = arcade.sprite_list.SpriteList()
        self.keys = set()

    def setup(self):
        player = Player()
        self.sprites.append(player)

    def on_draw(self):
        self.clear()
        self.sprites.draw()

    def on_update(self, delta_time):
        self.sprites.update(delta_time, self.keys)

    def on_key_press(self, symbol, modifiers):
        self.keys.add(symbol)

    def on_key_release(self, symbol, modifiers):
        self.keys.remove(symbol)


se
if __name__ == "__main__":
    print(arcade.color.AERO_BLUE)
    window = MainWindow(*WINDOW_SIZES, "Main")
    window.setup()
    arcade.run()
