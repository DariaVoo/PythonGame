from enemies.enemy import Enemy
from constats import SPRITE_SIZE, SPRITE_SCALING


class Worm(Enemy):
    def __init__(self, type_worm):
        if type_worm == 1:
            super().__init__(":resources:images/enemies/wormGreen.png", SPRITE_SCALING, SPRITE_SIZE,
                             SPRITE_SIZE, SPRITE_SIZE * 2)
        elif type_worm == 2:
            super().__init__(":resources:images/enemies/wormGreen.png", SPRITE_SCALING, SPRITE_SIZE,
                             SPRITE_SIZE * 4, SPRITE_SIZE * 4)
            self.boundary_right = SPRITE_SIZE * 8
            self.boundary_left = SPRITE_SIZE * 3
