import arcade

SPRITE_SCALING = 0.5


def create_player():
    player_sprite = arcade.Sprite(":resources:images/animated_characters/female_person/femalePerson_idle.png",
                                  SPRITE_SCALING)
    player_sprite.center_x = 300
    player_sprite.center_y = 400
    return player_sprite
