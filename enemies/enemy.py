import arcade


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
