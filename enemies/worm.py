from enemies.enemy import Enemy
from constants import SPRITE_SIZE, SPRITE_SCALING


class Worm(Enemy):
    def __init__(self, x=SPRITE_SIZE, y=SPRITE_SIZE * 2):
        super().__init__(":resources:images/enemies/wormGreen.png", SPRITE_SCALING, SPRITE_SIZE,
                         x, y)
