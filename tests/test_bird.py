import pytest
from bird import Bird

@pytest.mark.parametrize("x",[(10),(599)])
def test_init_barrier(x):
    test_bird= Bird(x)
    assert test_bird.block_x == x
    assert test_bird.block_y == 230
    assert test_bird.block_speed == 3
    assert test_bird.surf.get_size() == test_bird.rect.size
    assert test_bird.rect.x == x
    assert test_bird.rect.y == 230
    assert test_bird.surf.get_colorkey() == (255, 255, 255,255)

    assert test_bird.x == x
    assert test_bird.y == 180
    assert test_bird.speed == 3
    assert test_bird.cadr == 0
    assert test_bird.bird_surf.get_size() == test_bird.bird_rect.size
    assert test_bird.bird_rect.x == x
    assert test_bird.bird_rect.y == 180
    assert test_bird.bird_surf.get_colorkey() == (255, 255, 255, 255)


#@pytest.mark.parametrize("x",[(10),(599)])
def test_bird_move():
    test_bird = Bird(0)
    test_bird.move()
    assert test_bird.cadr == 1
    assert test_bird.x == -3
    assert test_bird.bird_surf.get_size() == test_bird.bird_rect.size
    assert test_bird.bird_rect.x == -3
    assert test_bird.bird_rect.y == 180
    assert test_bird.bird_surf.get_colorkey() == (255, 255, 255, 255)

    assert test_bird.surf.get_size() == test_bird.rect.size
    assert test_bird.rect.x == -3
    assert test_bird.rect.y == 230
    assert test_bird.surf.get_colorkey() == (255, 255, 255, 255)
    test_bird.cadr = 11
    test_bird.move()
    assert test_bird.cadr == 12
    test_bird.cadr = 21
    test_bird.move()
    assert test_bird.cadr == 1
