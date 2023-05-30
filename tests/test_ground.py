import pytest
from ground import Ground

@pytest.mark.parametrize("x", [0,23])
def test_init_barrier(x):
    block = Ground(x)
    assert block.x == x
    assert block.y == 230
    assert block.speed == 3
    assert block.surf.get_size() == block.rect.size
    assert block.rect.x == x
    assert block.rect.y == 230


@pytest.mark.parametrize("x,x_expected", [(0, -3), (23, 20)])
def test_move_barrier(x, x_expected):
    block = Ground(x)
    block.move()
    assert block.x == x_expected
    assert block.y == 230
    assert block.rect.x == x_expected
    assert block.rect.y == 230