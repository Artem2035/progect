import pytest
from terrain import Terrain
from ground import Ground
from barrier import Barrier
from bird import Bird

@pytest.mark.parametrize("terr_length, x_param",[(31,20)])
def test_init_terrain(terr_length,x_param):
    test_terrain = Terrain()
    assert len(test_terrain.terrain) == terr_length
    for i in range(terr_length):
        assert test_terrain.terrain[i].x == x_param*i

@pytest.mark.parametrize("terr_length",[(31)])
def test_check_terrain(terr_length):
    test_terrain = Terrain()
    test_terrain.ckeck_ground()
    assert test_terrain.terrain[0].x == 0
    for block in test_terrain.terrain:
        for i in range(7):
            block.move()
    assert test_terrain.terrain[0].x == -21
    test_terrain.ckeck_ground()
    assert len(test_terrain.terrain) == terr_length
    assert test_terrain.terrain[0].x == -1
    assert test_terrain.terrain[30].x == 599
    assert isinstance(test_terrain.terrain[30], Barrier) or isinstance(test_terrain.terrain[30], Bird)
    test_terrain.terrain[29],test_terrain.terrain[30] = test_terrain.terrain[30],test_terrain.terrain[29]
    for block in test_terrain.terrain:
        for i in range(7):
            block.move()
    test_terrain.ckeck_ground()
    assert isinstance(test_terrain.terrain[30], Ground)