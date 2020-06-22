from constants import SPRITE_SIZE, SPRITE_SCALING
from enemies.enemy import Enemy


class Saw(Enemy):
    def __init__(self, x=SPRITE_SIZE, y=SPRITE_SIZE * 2):
        super().__init__(":resources:images/enemies/saw.png", SPRITE_SCALING, SPRITE_SIZE,
                         x, y)
