import arcade
from consts import *
from views.start_view import StartView
from views.game_view import GameView


class MainWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)

    def setup(self):
        self._game = GameView()

        self._start = StartView(self, self._game)
        self.show_view(self._start)


if __name__ == "__main__":
    window = MainWindow(*WINDOW_SIZES, "Main")
    window.setup()
    arcade.run()
