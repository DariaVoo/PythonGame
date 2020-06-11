import arcade

from enemies.worm import Worm


def create_enemies(positions: list):
    enemy_list = arcade.SpriteList()
    type_worm = 1

    # (x, y)
    for pos in positions:
        enemy_list.append(Worm(type_worm))
        type_worm += 1
    return enemy_list
