from ability.ability import Ability
from ability.explosion import Explosion
from constants import BULLET_SPEED, SPRITE_SCALING_LASER


class Bullet(Ability):
    def __init__(self, player_x, player_y):
        # Create a bullet
        super().__init__(":resources:images/space_shooter/laserBlue01.png", SPRITE_SCALING_LASER,
                         player_x, player_y, BULLET_SPEED)

        # Изображение лазера будет прямое, поэтому угол наклона изображения 0
        self.angle = 0

    def clone(self, player_x, player_y):
        return Bullet(player_x, player_y)

    def attack(self, hit_list, explosion_texture_list, explosions_list):
        """ Прорисока атаки """
        # If it did...
        # Make an explosion
        explosion = Explosion(explosion_texture_list)

        # Move it to the location of the coin
        explosion.center_x = hit_list[0].center_x
        explosion.center_y = hit_list[0].center_y

        # Call update() because it sets which image we start on
        explosion.update()

        # Add to a list of sprites that are explosions
        explosions_list.append(explosion)
