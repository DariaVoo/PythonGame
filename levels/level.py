from levels import genlvl
from levels.genlvl import genlvl


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


def create_lvl(lvl=1):
    """
    Создание карты уровня. По факту - наполнение wall_list
    """
    levels = {
        1: ":resources:images/tiles/boxCrate_double.png",
        2: ":resources:images/tiles/brickGrey.png",
        3: ":resources:images/tiles/planetHalf.png",
        4: ":resources:images/tiles/snowHalf.png",
        5: ":resources:images/tiles/stoneHalf.png",
        6: ":resources:images/tiles/sandHalf.png",
        7: ":resources:images/tiles/dirtHalf.png",
        8: ":resources:images/tiles/brickBrown.png",
        9: ":resources:images/tiles/bridgeA.png",
    }
    box = levels.get(lvl % 10)

    return genlvl(box)

    # wall_list = arcade.SpriteList()
    # # ДОЛЖНО ГЕНЕРИРОВАТЬСЯ
    # x = y = 0  # координаты
    # for row in level:  # вся строка
    #     for col in row:  # каждый символ
    #         if col == "-":
    #             # создаем блок
    #             wall = arcade.Sprite(box, SPRITE_SCALING)
    #             wall.center_x = x
    #             wall.center_y = y
    #             wall_list.append(wall)
    #
    #         x += wall._get_width()  # блоки платформы ставятся на ширине блоков
    #     y += wall._get_height()  # то же самое и с высотой
    #     x = 0  # на каждой новой строчке начинаем с нуля
    #
    # # Ставим монеты на карту
    # coin_list = arcade.SpriteList()
    # # ДОЛЖНО ГЕНЕРИРОВАТЬСЯ
    # for i in range(15):
    #     # Create the coin instance
    #     # Coin image from kenney.nl
    #     coin = arcade.Sprite(":resources:images/items/coinGold.png", SPRITE_SCALING_COIN)
    #
    #     # Position the coin
    #     coin.center_x = random.randrange(SCREEN_WIDTH)
    #     coin.center_y = random.randrange(120, SCREEN_HEIGHT)
    #
    #     # Add the coin to the lists
    #     coin_list.append(coin)
    #
    # # ДОЛЖНО ГЕНЕРИРОВАТЬСЯ
    # pos_ability = [Position(200, 400, 1), Position(700, 300, 2), Position(900, 500, 3)]
    # # Ставим способности на карту
    # ability_list = ability_factory(pos_ability)
    # # ДОЛЖНО ГЕНЕРИРОВАТЬСЯ
    # pos_enemies = [Position(100, 300, 1), Position(500, 500, 2), Position(900, 700, 3)]
    # # Ставим врагов
    # enemy_list = create_enemies(pos_enemies)
    #
    # return wall_list, coin_list, ability_list, enemy_list
