import random

import arcade

from constants import SPRITE_SCALING_COIN

SPRITE_SCALING = 0.4
# Для enemy
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

END_OF_MAP = 25 * 51.2 # ЭТО НУЖНО ИСПРАВИТЬ сейча это просто колво блоков на wall.ghet_width
lvl1 = [
    "-------------------------",
    "-                       -",
    "-   -                   -",
    "-          -            -",  # и тут лагает
    "-            --         -",  # здесь лагает почему-то
    "-      -                 ",
    "--                       ",
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
    "-                        ",
    "-                       -",
    "-------------------------"]

lvl2 = [
    "-------------------------",
    "-                       -",
    "-   ---------------     -",
    "-          ------       -",  # и тут лагает
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


def create_lvl(wall_list: arcade.SpriteList, coin_list: arcade.SpriteList, lvl=1):
    """
    Создание карты уровня. По факту - наполнение wall_list
    !!!! карта строится вверх ногами (если смотреть на массив)
    """
    level = lvl1 if lvl == 1 else lvl2
    box = ":resources:images/tiles/boxCrate_double.png" if lvl == 1 else ":resources:images/tiles/brickGrey.png"

    x = y = 0  # координаты
    for row in level:  # вся строка
        for col in row:  # каждый символ
            if col == "-":
                # создаем блок, заливаем его цветом и рисеум его
                wall = arcade.Sprite(box, SPRITE_SCALING)
                wall.center_x = x
                wall.center_y = y
                wall_list.append(wall)

            x += wall._get_width()  # блоки платформы ставятся на ширине блоков
        y += wall._get_height()  # то же самое и с высотой
        x = 0  # на каждой новой строчке начинаем с нуля

    # Ставим монеты на карту
    # Create the coins
    for i in range(15):
        # Create the coin instance
        # Coin image from kenney.nl
        coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)

        # Position the coin
        coin.center_x = random.randrange(SCREEN_WIDTH)
        coin.center_y = random.randrange(120, SCREEN_HEIGHT)

        # Add the coin to the lists
        coin_list.append(coin)
