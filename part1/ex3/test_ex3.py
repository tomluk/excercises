from part1.ex3.ex3 import flip_coins
import pytest


def test_flip_coins1():
    """
    Test verifies short sequence of coins.
    """
    sequence = [0, 1, 1, 0]
    assert 2 == flip_coins(sequence)


def test_flip_coins2():
    """
    Test verifies exception it thrown once the sequence is empty
    """
    sequence = []
    with pytest.raises(BaseException, match="provided sequence to short"):
        flip_coins(sequence)


def test_flip_coins3():
    """
    Test verifies exception it thrown once the sequence is empty
    """
    sequence = [1]
    with pytest.raises(BaseException, match="provided sequence to short"):
        flip_coins(sequence)


def test_flip_coins4():
    """
    Test verifies no flips are required
    """
    sequence = [1, 0]
    assert 0 == flip_coins(sequence)


def test_flip_coins5():
    """
    Test verifies short sequence
    """
    sequence = [1, 1]
    assert 1 == flip_coins(sequence)


def test_flip_coins6():
    """
    Test verifies sequence full of 1
    """
    sequence = [1, 1, 1, 1, 1, 1, 1]
    assert 3 == flip_coins(sequence)


def test_flip_coins7():
    """
    Test verifies sequence full of 0
    """
    sequence = [0, 0, 0, 0, 0, 0, 0]
    assert 3 == flip_coins(sequence)


def test_flip_coins8():
    """
    Test verifies sequence full of 0
    """
    sequence = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1,
                0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
    assert 0 == flip_coins(sequence)
