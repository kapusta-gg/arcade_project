import arcade
import arcade.gui
from consts import *


class SettingsView(arcade.View):

    def __init__(self, _window: arcade.Window, _main: arcade.View):
        super().__init__()
        self._main = _main
        self._window = _window

        self.manager = arcade.gui.UIManager()
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self.setup_ui()
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.AERO_BLUE)

    def setup_ui(self):
        '''Настривает UI главного окна'''

        grid = arcade.gui.UIGridLayout(column_count=1, row_count=2,
                                       horizontal_spacing=20, vertical_spacing=20)

        sett_grid = arcade.gui.UIGridLayout(column_count=2, row_count=2,
                                            horizontal_spacing=20, vertical_spacing=20)

        window_size_t = arcade.gui.UILabel(
            text="Размеры окна", width=50, text_color=arcade.color.RED)
        window_size = arcade.gui.UIDropdown(
            options=WINDOWS_OPTIONS, width=100, default=WINDOWS_OPTIONS[0])

        window_size.on_change = self.change_window

        back_btn = arcade.gui.UIFlatButton(text="Назад", width=100)

        back_btn.on_click = self.back

        sett_grid.add(window_size_t, column=0, row=0)
        sett_grid.add(window_size, column=1, row=0)

        grid.add(sett_grid, column=0, row=0)
        grid.add(back_btn, column=0, row=1)
        self.anchor.add(child=grid, anchor_x="center_x", anchor_y="center_y")

    def change_window(self, event):
        x, y = list(map(int, event.new_value.split("x")))
        self._window.size = (x, y)

    def back(self, event):
        self._main.update_ui()
        self._window.show_view(self._main)

    def on_show_view(self):
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()
        self.manager.draw()
