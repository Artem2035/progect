import pytest
import time
from dino import Dino
from terrain import Terrain
from barrier import Barrier
from bird import Bird

def test_init_barrier():
    test_dino = Dino()
    assert test_dino.x == 0
    assert test_dino.y == 200
    assert test_dino.speed == 0
    assert test_dino.cadr == 0
    assert test_dino.state == "run"
    assert test_dino.dino_surf.get_colorkey() == (255, 255, 255, 255)
    assert test_dino.start_anim_jump == 0
    assert test_dino.dino_rect.x == 0
    assert test_dino.dino_rect.y == 200
    assert test_dino.dino_rect.size == (27, 36)


@pytest.mark.parametrize("y,expected_y", [(-3, 197), (3, 203)])
def test_dino_jump(y, expected_y):
    test_dino = Dino()
    test_dino.jump(y)
    assert test_dino.x == 0
    assert test_dino.y == expected_y


@pytest.mark.parametrize("v, expected_speed", [(-3, -3), (3, 3)])
def test_dino_speed_change(v, expected_speed):
    test_dino = Dino()
    test_dino.change_speed(v)
    assert test_dino.speed == expected_speed


@pytest.mark.parametrize("state, expected_state", [("run", "run"), ("tilt", "tilt"),
                                                   ("jump", "jump"), ("df", "run"), ("", "run")])
def test_dino_speed_change(state, expected_state):
    test_dino = Dino()
    test_dino.change_state(state)
    assert test_dino.state == expected_state


@pytest.mark.parametrize("v,x, expected_x", [(-3, 0, 0), (3, 0, 3), (3, 498, 498)])
def test_dino_move_run(v, x, expected_x):
    test_dino = Dino()
    test_dino.x = x
    test_dino.change_speed(v)
    test_dino.move()
    assert test_dino.cadr == 1
    assert test_dino.y == 200
    assert test_dino.dino_surf.get_colorkey() == (255, 255, 255, 255)
    assert test_dino.dino_rect.x == expected_x
    assert test_dino.dino_rect.y == 200
    assert test_dino.dino_rect.size == (27, 36)


def test_dino_move_jump():
    test_dino = Dino()
    test_dino.set_start_anim_time()
    test_dino.change_state("jump")
    test_dino.move()
    test_dino.move()
    assert test_dino.y == 194
    assert test_dino.x == 0
    time.sleep(1)
    test_dino.move()
    assert test_dino.y == 197
    time.sleep(1)
    test_dino.move()
    assert test_dino.state == "run"
    assert test_dino.y == 200
    assert test_dino.start_anim_jump == 0


def test_dino_move_tilt():
    test_dino = Dino()
    test_dino.change_state("tilt")
    test_dino.move()
    assert test_dino.y == 217
    assert test_dino.cadr == 1
    test_dino.cadr = 21
    test_dino.move()
    assert test_dino.cadr == 1


def test_dino_collision():
    test_dino = Dino()
    test_terr = Terrain()
    assert test_dino.dino_surf.get_colorkey() == (255, 255, 255, 255)
    assert not test_dino.collision(test_terr.terrain)
    test_terr.terrain[1] = Bird(20)
    assert test_dino.collision(test_terr.terrain)
    test_dino.change_state("tilt")
    test_terr.terrain[1] = Barrier(20)
    assert test_dino.collision(test_terr.terrain)
    assert test_dino.y == 200
    assert test_dino.x == 10
    assert test_dino.dino_rect.x == 10
    assert test_dino.dino_rect.y == 183
