from abc import abstractmethod

import arcade


class Ability(arcade.Sprite):
    def __init__(self, img: str, scale: int, x, y, speed):
        super().__init__(img, scale)
        # Position
        self.center_x = x
        self.center_y = y
        self.speed = speed

    def set_position_and_speed(self, player_x, player_y):
        self.center_x = player_x
        self.center_y = player_y
        self.change_x = self.speed

    @abstractmethod
    def attack(self):
        pass

