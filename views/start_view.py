import arcade
import arcade.gui


class StartView(arcade.View):

    def __init__(self, _window: arcade.Window, _game: arcade.View):
        '''
        :param _window: Объект arcade.Window для переключения окон
        :type _window: arcade.Window
        :param _game: Окно для переключения на игру
        :type _game: arcade.View
        '''
        super().__init__()
        self.manager = arcade.gui.UIManager()
        self.anchor = self.manager.add(arcade.gui.UIAnchorLayout())

        self._game = _game
        self._window = _window

        self.setup_ui()
        self.setup()

    def setup(self):
        arcade.set_background_color(arcade.color.AERO_BLUE)

    def setup_ui(self):
        '''Настривает UI главного окна'''

        # Слой
        grid = arcade.gui.UIGridLayout(column_count=1, row_count=2,
                                       horizontal_spacing=20, vertical_spacing=20)

        # Кнопка начала игры
        play_btn = arcade.gui.UIFlatButton(text="Играть", width=100)

        play_btn.on_click = self.game_open

        # Кнопка закрытия игры
        close_btn = arcade.gui.UIFlatButton(text="Выйти", width=100)

        close_btn.on_click = self.close

        grid.add(play_btn, column=0, row=0)
        grid.add(close_btn, column=0, row=1)
        self.anchor.add(child=grid, anchor_x="center_x", anchor_y="center_y")

    def game_open(self, event):
        self._game.setup()
        self._window.show_view(self._game)

    def close(event):
        self._window.close()

    def on_show_view(self):
        self.manager.enable()

    def on_hide_view(self):
        self.manager.disable()

    def on_draw(self):
        self.clear()
        self.manager.draw()
