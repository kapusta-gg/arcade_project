import arcade
from entites.player import Player


class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.sprites = arcade.sprite_list.SpriteList()
        self.keys = set()
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.FERN_GREEN)
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
