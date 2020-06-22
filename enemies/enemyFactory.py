import arcade

from enemies.saw import Saw
from enemies.slime import Slime
from enemies.worm import Worm


def create_enemies(positions: list):
    enemy_list = arcade.SpriteList()

    # (x, y, type)
    for pos in positions:
        enemy_list.append(create_ability(pos.x, pos.y, pos.type_sprite))
    return enemy_list


def create_ability(x: int, y: int, type_ability: int, ):
    if type_ability == 1:
        return Worm(x, y)
    elif type_ability == 2:
        return Slime(x, y)
    elif type_ability == 3:
        return Saw(x, y)