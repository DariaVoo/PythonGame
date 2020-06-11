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
    def __init__(self, img, scale, size, x, y):
        super().__init__(img, scale)
        self.bottom = y
        self.left = x


