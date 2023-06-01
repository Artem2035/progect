import pytest
from game import Game


def test_init_game():
    g1 = Game()
    assert g1.back_color == (255, 255, 255)
    assert g1.best_score_color == (255, 126, 83)
    assert g1.score_color == (127, 127, 127)
    assert g1.size == (600, 300)
    assert g1.FPS == 30
    assert g1.score == 0
    assert g1.running == True
    assert g1.surf.get_size() == g1.button_rect.size
    assert g1.button_rect.x == 264
    assert g1.button_rect.y == 118
    assert g1.surf.get_colorkey() == (255, 255, 255, 255)

