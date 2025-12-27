import arcade
import json
import arcade.gui
from consts import *


def rewrite_settings(key: str, data_):
    with open("settings.json", "r") as r:
        data = json.load(r)
        data["settings"][key] = data_
    with open("settings.json", "w") as w:
        w.write(json.dumps(data, indent=4))


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
        temp = "x".join(map(str, self._window.size))
        window_size = arcade.gui.UIDropdown(
            options=WINDOWS_OPTIONS, width=100, default=temp)

        sound_vol_t = arcade.gui.UILabel(
            text="Громкость музыки", width=50, text_color=arcade.color.RED)
        temp = "x".join(map(str, self._window.size))
        sound_vol = arcade.gui.UISlider(
            value=SOUND_VOLUME, min_value=0, max_value=10, width=100, step=1)

        window_size.on_change = self.change_window
        sound_vol.on_change = self.change_volume

        back_btn = arcade.gui.UIFlatButton(text="Назад", width=100)

        back_btn.on_click = self.back

        sett_grid.add(window_size_t, column=0, row=0)
        sett_grid.add(window_size, column=1, row=0)
        sett_grid.add(sound_vol_t, column=0, row=1)
        sett_grid.add(sound_vol, column=1, row=1)

        grid.add(sett_grid, column=0, row=0)
        grid.add(back_btn, column=0, row=1)
        self.anchor.add(child=grid, anchor_x="center_x", anchor_y="center_y")

    def change_window(self, event):
        x, y = list(map(int, event.new_value.split("x")))
        rewrite_settings("window_sizes", [x, y])
        self._window.size = (x, y)

    def change_volume(self, event):
        v = event.new_value
        rewrite_settings("volume", v)
        self._main.game_volume = v

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
