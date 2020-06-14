import arcade

from ability.bullet import Bullet
from constants import SPRITE_SCALING, MOVEMENT_SPEED, JUMP_SPEED, SCREEN_HEIGHT


class Player(arcade.Sprite):
    """
    @x, @y - start position
    """
    def __init__(self, x=600, y=400):
        super().__init__(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                         SPRITE_SCALING)
        self.center_x = x
        self.center_y = y
        self.ability_list = arcade.SpriteList()

    def move(self, key, jump):
        if key == arcade.key.UP:
            if jump:
                self.change_y = JUMP_SPEED
        elif key == arcade.key.DOWN:
            self.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.change_x = MOVEMENT_SPEED

    def add_ability(self):
        bullet = Bullet(self.center_x, self.center_y)
        self.ability_list.append(bullet)

    def attack(self, enemy_list, score, explosion_texture_list, explosions_list):
        # Loop through each bullet
        for bullet in self.ability_list:

            # Check this bullet to see if it hit a coin
            hit_list = arcade.check_for_collision_with_list(bullet, enemy_list)

            # If it did, get rid of the bullet
            if len(hit_list) > 0:
                bullet.attack(hit_list, explosion_texture_list, explosions_list)

                # Get rid of the bullet
                bullet.remove_from_sprite_lists()

            # For every coin we hit, add to the score and remove the coin
            for enemy in hit_list:
                enemy.remove_from_sprite_lists()
                score += 5

            # If the bullet flies off-screen, remove it.
            if bullet.bottom > SCREEN_HEIGHT:
                bullet.remove_from_sprite_lists()

        return score
