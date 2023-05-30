import pytest
#from cloud import Cloud


@pytest.mark.parametrize("x", [0,23])
def test_init_cloud(x):
    cloud1 = Cloud(x)
    assert cloud1.x == x
    assert 75 <= cloud1.y <=100
    assert cloud1.speed == 4
    assert cloud1.surf.get_size() == cloud1.rect.size
    assert cloud1.rect.x == x
    assert 75 <= cloud1.rect.y <=100


@pytest.mark.parametrize("x,x_expected", [(0, -4), (23, 19)])
def test_move_cloud(x, x_expected):
    cloud1 = Cloud(x)
    y_expected = cloud1.y
    cloud1.move()
    assert cloud1.x == x_expected
    assert cloud1.y == y_expected
    assert cloud1.rect.x == x_expected
    assert cloud1.rect.y == y_expected

@pytest.mark.parametrize("x,x_expected", [(-53, 600), (23, 23)])
def test_check_cloud(x, x_expected):
    cloud1 = Cloud(x)
    cloud1.check()
    assert cloud1.x == x_expected
    assert 75 <= cloud1.rect.y <=100
print("100%")
