import arcade

from ability.bullet import Bullet
from ability.rock import Rock


def ability_factory(positions: list):
    ability_list = arcade.SpriteList()

    # (x, y, type)
    for pos in positions:
        ability_list.append(create_ability(pos.x, pos.y, pos.type_sprite))
    return ability_list


def create_ability(x: int, y: int, type_ability: int,):
    if type_ability == 1:
        return Bullet(x, y)
    elif type_ability == 2:
        return Rock(x, y)

