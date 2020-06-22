from abc import abstractmethod

import arcade


class Ability(arcade.Sprite):
    def __init__(self, img: str, scale: int, x, y, speed):
        super().__init__(img, scale)
        # Position
        self.center_x = x
        self.center_y = y
        self.change_x = speed

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def clone(self, player_x, player_y):
        """ Метод прототипа """
        pass
