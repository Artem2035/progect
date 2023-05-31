from test import f
import pytest

def test_tst1():
    assert f(3,4) == 7

def test_tst2():
    assert f(-1, 2) == 1

def test_tst3():
    assert f(-3, -4) == -7

def test_tst4():
    assert f(0, 0) == 0