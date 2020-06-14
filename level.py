import arcade

from constats import COIN_SCALING

SPRITE_SCALING = 0.4
# Для enemy
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

lvl1 = [
    "-------------------------",
    "-                       -",
    "-   -                   -",
    "-          -            -",  # и тут лагает
    "-            --         -",  # здесь лагает почему-то
    "-      -                -",
    "--                      -",
    "-         -             -",
    "-              -    --- -",
    "-            -          -",
    "-                -      -",
    "-      ---             --",
    "-                  -    -",
    "-   -----------        --",
    "-                   -   -",
    "-                -      -",
    "-                   --  -",
    "-                       -",
    "-                       -",
    "-------------------------"]


def create_lvl(wall_list: arcade.SpriteList, coin_list: arcade.SpriteList):
    """
    Создание карты уровня. По факту - наполнение wall_list
    !!!! карта строится вверх ногами (если смотреть на массив)
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

    # Ставим монеты на карту
    for x in range(SPRITE_SIZE, 1250 - SPRITE_SIZE, 128):
        coin = arcade.Sprite(":resources:images/items/coinGold.png", COIN_SCALING)
        coin.center_x = x
        coin.center_y = 96
        coin_list.append(coin)

    # # Draw the walls on the bottom Добавляем землю
    # for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
    #     wall = arcade.Sprite(":resources:images/tiles/grassMid.png", SPRITE_SCALING)
    #
    #     wall.bottom = 0
    #     wall.left = x
    #     wall_list.append(wall)
