from abc import abstractmethod

import arcade


class Ability(arcade.Sprite):
    def __init__(self, img: str, scale: int, player_x, player_y, speed):
        super().__init__(img, scale)
        # Position
        self.center_x = player_x
        self.center_y = player_y
        self.change_x = speed

    @abstractmethod
    def attack(self):
        pass

