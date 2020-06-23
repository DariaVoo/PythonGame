import arcade

from ability.bullet import Bullet
from ability.rock import Rock
from ability.star import Star


def ability_factory(positions: list, wall_list):
    ability_list = arcade.SpriteList()

    # (x, y, type)
    for pos in positions:
        abil = create_ability(pos.x, pos.y, pos.type_sprite)
        if len(arcade.check_for_collision_with_list(abil, wall_list)) == 0:
            ability_list.append(abil)
    return ability_list


def create_ability(x: int, y: int, type_ability: int,):
    if type_ability == 1:
        return Bullet(x, y)
    elif type_ability == 2:
        return Rock(x, y)
    elif type_ability == 3:
        return Star(x, y)

