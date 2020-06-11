import arcade
import os

# Число для уменьшения изображения
from enemies.enemyFactory import create_enemies
from level import create_lvl
from player import Player
from constats import *


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.coin_list: arcade.SpriteList = None
        self.wall_list: arcade.SpriteList = None
        self.player_list: arcade.SpriteList = None
        self.enemy_list: arcade.SpriteList = None

        # Set up the player
        self.player_sprite: Player = None
        self.physics_engine = None
        self.game_over = False

        # sсroll(move camera)
        self.view_left = 0
        self.view_bottom = 0

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()  # Список стен, через которые игрок не может проходить
        self.enemy_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = Player()
        self.player_list.append(self.player_sprite)
        # Set up the enemies
        self.enemy_list = create_enemies([1, 2])

        # Set up the walls
        create_lvl(self.wall_list)

        # Физический движок для платформера
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        # Очищаем окно и начинаем отрисовку
        arcade.start_render()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.enemy_list.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        self.player_sprite.move(key, self.physics_engine.can_jump())

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Update the player based on the physics engine
        if not self.game_over:
            # Move the enemies
            self.enemy_list.update()

            # Check each enemy
            for enemy in self.enemy_list:
                enemy.move(self.wall_list)

            # Обновляем игрока используя физический движок
            self.physics_engine.update()

            # See if the player hit a worm. If so, game over.
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)) > 0:
                self.game_over = True

            # --- Manage Scrolling ---
            # Track if we need to change the view port
            changed = False

            # Scroll left
            left_bndry = self.view_left + VIEWPORT_LEFT_MARGIN
            if self.player_sprite.left < left_bndry:
                self.view_left -= left_bndry - self.player_sprite.left
                changed = True

            # Scroll right
            right_bndry = self.view_left + SCREEN_WIDTH - VIEWPORT_RIGHT_MARGIN
            if self.player_sprite.right > right_bndry:
                self.view_left += self.player_sprite.right - right_bndry
                changed = True

            # Scroll up
            top_bndry = self.view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN_TOP
            if self.player_sprite.top > top_bndry:
                self.view_bottom += self.player_sprite.top - top_bndry
                changed = True

            # Scroll down
            bottom_bndry = self.view_bottom + VIEWPORT_MARGIN_BOTTOM
            if self.player_sprite.bottom < bottom_bndry:
                self.view_bottom -= bottom_bndry - self.player_sprite.bottom
                changed = True

            # If we need to scroll, go ahead and do it.
            if changed:
                self.view_left = int(self.view_left)
                self.view_bottom = int(self.view_bottom)
                arcade.set_viewport(self.view_left,
                                    SCREEN_WIDTH + self.view_left,
                                    self.view_bottom,
                                    SCREEN_HEIGHT + self.view_bottom)


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
