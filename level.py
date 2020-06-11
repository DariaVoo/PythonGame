import arcade

SPRITE_SCALING = 0.4
# Для enemy
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

lvl1 = [
    "-------------------------",
    "-                       -",
    "-                       -",
    "-                       -",
    "-            --         -",
    "-                       -",
    "--                      -",
    "-                       -",
    "-                   --- -",
    "-                       -",
    "-                       -",
    "-      ---              -",
    "-                       -",
    "-   -----------        -",
    "-                       -",
    "-                -      -",
    "-                   --  -",
    "-                       -",
    "-                       -",
    "-------------------------"]


def create_lvl(wall_list: arcade.SpriteList):
    """
    Создание карты уровня. По факту - наполнение wall_list
    """
    level = lvl1
    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                # создаем блок, заливаем его цветом и рисеум его
                wall = arcade.Sprite(":resources:images/tiles/boxCrate_double.png", SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                wall_list.append(wall)

            x += wall._get_width()  # блоки платформы ставятся на ширине блоков
        y += wall._get_height()  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    # # Draw the walls on the bottom Добавляем землю
    # for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
    #     wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)
    #
    #     wall.bottom = 0
    #     wall.left = x
    #     wall_list.append(wall)
