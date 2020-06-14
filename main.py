import arcade

from UI_view.menu import MenuView
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE


def main():
    """ Main method """
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.total_score = 0
    start_view = MenuView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()