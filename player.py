import arcade

from constats import SPRITE_SCALING, MOVEMENT_SPEED, JUMP_SPEED


class Player(arcade.Sprite):
    """
    @x, @y - start position
    """

    def __init__(self, x=600, y=400):
        super().__init__(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                         SPRITE_SCALING)
        self.center_x = x
        self.center_y = y
        self

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

