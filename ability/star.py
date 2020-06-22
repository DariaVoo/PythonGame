from ability.ability import Ability
from ability.explosion import Explosion
from constants import BULLET_SPEED, SPRITE_SCALING_STAR


class Star(Ability):
    def __init__(self, player_x, player_y):
        super().__init__(":resources:images/items/star.png", SPRITE_SCALING_STAR,
                         player_x, player_y, BULLET_SPEED)

    def clone(self, player_x, player_y):
        return Star(player_x, player_y)

    def attack(self, hit_list, explosion_texture_list, explosions_list):
        """ Прорисока атаки """
        # Make an explosion
        explosion = Explosion(explosion_texture_list)

        # Move it to the location of the coin
        explosion.center_x = hit_list[0].center_x
        explosion.center_y = hit_list[0].center_y

        # Call update() because it sets which image we start on
        explosion.update()

        # Add to a list of sprites that are explosions
        explosions_list.append(explosion)
