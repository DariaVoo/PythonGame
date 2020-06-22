import arcade

from constants import VIEWPORT_MARGIN_BOTTOM, SCREEN_HEIGHT, VIEWPORT_MARGIN_TOP, SCREEN_WIDTH, VIEWPORT_RIGHT_MARGIN, \
    VIEWPORT_LEFT_MARGIN


def scroll_manage(player_sprite: arcade.Sprite, view_left, view_bottom):
    # Track if we need to change the view port
    changed = False

    # Scroll left
    left_bndry = view_left + VIEWPORT_LEFT_MARGIN
    if player_sprite.left < left_bndry:
        view_left -= left_bndry - player_sprite.left
        changed = True

    # Scroll right
    right_bndry = view_left + SCREEN_WIDTH - VIEWPORT_RIGHT_MARGIN
    if player_sprite.right > right_bndry:
        view_left += player_sprite.right - right_bndry
        changed = True

    # Scroll up
    top_bndry = view_bottom + SCREEN_HEIGHT - VIEWPORT_MARGIN_TOP
    if player_sprite.top > top_bndry:
        view_bottom += player_sprite.top - top_bndry
        changed = True

    # Scroll down
    bottom_bndry = view_bottom + VIEWPORT_MARGIN_BOTTOM
    if player_sprite.bottom < bottom_bndry:
        view_bottom -= bottom_bndry - player_sprite.bottom
        changed = True

    # If we need to scroll, go ahead and do it.
    if changed:
        view_left = int(view_left)
        view_bottom = int(view_bottom)
        arcade.set_viewport(view_left,
                            SCREEN_WIDTH + view_left,
                            view_bottom,
                            SCREEN_HEIGHT + view_bottom)

    return view_left, view_bottom
