import arcade
import os

# Число для уменьшения изображения
from enemy import create_enemy2, create_enemy1
from level import create_lvl
from player import create_player

SPRITE_SCALING = 0.5
GRAVITY = .9 * SPRITE_SCALING
# Для enemy
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Walls Example"

MOVEMENT_SPEED = 5
JUMP_SPEED = 14


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
        self.player_sprite = None
        self.physics_engine = None

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()  # Список стен, через которые игрок не может проходить
        self.enemy_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = create_player()
        self.player_list.append(self.player_sprite)
        # Set up the player
        self.enemy_list.append(create_enemy1())
        self.enemy_list.append(create_enemy2())


        # -- Set up the walls
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

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Move the enemies
        self.enemy_list.update()

        # Check each enemy
        for enemy in self.enemy_list:
            # If the enemy hit a wall, reverse
            if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                enemy.change_x *= -1
            # If the enemy hit the left boundary, reverse
            elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                enemy.change_x *= -1
            # If the enemy hit the right boundary, reverse
            elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                enemy.change_x *= -1

        # Обновляем игрока использую физический движок
        self.physics_engine.update()


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
