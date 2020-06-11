import arcade

SPRITE_SCALING = 0.5
# Для enemy
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)


def create_enemy1():
    # -- Draw an enemy on the ground
    enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

    enemy.bottom = SPRITE_SIZE
    enemy.left = SPRITE_SIZE * 2

    # Set enemy initial speed
    enemy.change_x = 2
    return enemy


def create_enemy2():
    # -- Draw a enemy on the platform
    enemy = arcade.Sprite(":resources:images/enemies/wormGreen.png", SPRITE_SCALING)

    enemy.bottom = SPRITE_SIZE * 4
    enemy.left = SPRITE_SIZE * 4

    # Set boundaries on the left/right the enemy can't cross
    enemy.boundary_right = SPRITE_SIZE * 8
    enemy.boundary_left = SPRITE_SIZE * 3
    enemy.change_x = 2
    return enemy


class Enemy(arcade.Sprite):
    def __init__(self, img, scale, size, x, y, speed=2):
        super().__init__(img, scale)
        self.bottom = y
        self.left = x
        self.change_x = speed

    def move(self, wall_list):
        # If the enemy hit a wall, reverse
        if len(arcade.check_for_collision_with_list(self, wall_list)) > 0:
            self.change_x *= -1
        # If the enemy hit the left boundary, reverse
        elif self.boundary_left is not None and self.left < self.boundary_left:
            self.change_x *= -1
        # If the enemy hit the right boundary, reverse
        elif self.boundary_right is not None and self.right > self.boundary_right:
            self.change_x *= -1


class Worm(Enemy):
    def __init__(self, type):
        if type == 1:
            super().__init__(":resources:images/enemies/wormGreen.png", SPRITE_SCALING, SPRITE_SIZE,
                         SPRITE_SIZE, SPRITE_SIZE * 2)
        elif type == 2:
            super().__init__(":resources:images/enemies/wormGreen.png", SPRITE_SCALING, SPRITE_SIZE,
                             SPRITE_SIZE * 4, SPRITE_SIZE * 4)
            self.boundary_right = SPRITE_SIZE * 8
            self.boundary_left = SPRITE_SIZE * 3
