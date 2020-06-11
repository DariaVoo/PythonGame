import arcade

SPRITE_SCALING = 0.5
# Для enemy
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


def create_lvl(wall_list: arcade.SpriteList):
    """
    Создание карты уровня. По факту - наполнение wall_list
    """
    # Create a row of boxes
    for x in range(173, 650, 64):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = 200
        wall_list.append(wall)

    # Create a column of boxes
    for y in range(273, 500, 64):
        wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
        wall.center_x = 465
        wall.center_y = y
        wall_list.append(wall)

    # Draw the walls on the bottom Добавляем землю
    for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
        wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)

        wall.bottom = 0
        wall.left = x
        wall_list.append(wall)
