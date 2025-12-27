import arcade
from consts import *
from views.start_view import StartView


class MainWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=False)

    def setup(self):
        self._start = StartView(self)
        self.show_view(self._start)


if __name__ == "__main__":
    window = MainWindow(*get_settings("window_sizes"), "Main")
    window.setup()
    arcade.run()
