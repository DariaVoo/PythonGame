import os

import arcade

from UI_view.instruction import InstructionView
from constants import SCREEN_HEIGHT, SCREEN_WIDTH


class MenuView(arcade.View):
    def __init__(self):
        super().__init__()
        # Background image will be stored in this variable
        self.background = None

        img_path = os.path.dirname(os.path.abspath(__file__))
        img_path += "/menu_screen.jpg"
        self.background = arcade.load_texture(img_path)

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

        # Выгрузка изображения на экран
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)
