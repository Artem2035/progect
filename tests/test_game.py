import pytest
from game import Game


def test_init_Game():
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

    # self.player = Dino()
    # self.game_terrain = Terrain()
    # self.sky = [Cloud(600), Cloud(600 + random.randint(100, 300)), Cloud(600 + random.randint(350, 450))]
    #
    # # retry_button
    # self.surf = pygame.image.load('assets/retry_button.png')
    # self.surf.set_colorkey((255, 255, 255))
    # self.button_rect = self.surf.get_rect()
    # self.button_rect = self.button_rect.move(264, 118)