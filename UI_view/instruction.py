import os

import arcade

from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logic.game import GameView


class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()
        # Background image will be stored in this variable
        self.background = None

        img_path = os.path.dirname(os.path.abspath(__file__))
        img_path += "/instruction.jpg"
        self.background = arcade.load_texture(img_path)

    def on_show(self):
        """ This is run once when we switch to this view """
        arcade.set_background_color(arcade.csscolor.DARK_SLATE_BLUE)

        # Reset the viewport, necessary if we have a scrolling game and we need
        # to reset the viewport back to the start so we can see what we draw.
        arcade.set_viewport(0, SCREEN_WIDTH - 1, 0, SCREEN_HEIGHT - 1)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)


    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)