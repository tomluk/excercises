from part1.ex1.ex1 import first_repeated
import pytest

def test_first_repeated_no_repeated():
    """
    test verifies there is no repeated number on the same index in two vectors
    """
    vec1 = [1, 2, 3, 4]
    vec2 = [4, 3, 2, 1]
    assert first_repeated(vec1, vec2) == -1


def test_first_repeated_vec1_empty():
    """
    test verifies empty list
    """
    vec1 = []
    vec2 = [4, 3, 2, 1]
    with pytest.raises(BaseException, match="Lenght of vector is 0"):
        first_repeated(vec1, vec2)


def test_first_repeated_vec2_empty():
    """
    test verifies empty list
    """
    vec1 = [1, 2, 3, 4]
    vec2 = []
    with pytest.raises(BaseException, match="Lenght of vector is 0"):
        first_repeated(vec1, vec2)


def test_first_repeated_wrong_data_type():
    """
    test verifies wrong data type in vec2
    """
    vec1 = [1, 2, 3, 4]
    vec2 = ["a", "b", (0, 1, 2)]
    with pytest.raises(TypeError, match="Not all elements in vector type int"):
        first_repeated(vec1, vec2)


def test_first_repeated_on_first_index():
    """
    test verifies repeated number on first index
    """
    vec1 = [2, 2, 3, 4]
    vec2 = [2, 3, 4]
    assert first_repeated(vec1, vec2) == 2


def test_first_repeated_on_4th_index():
    """
    test verifies repeated number on first index
    """
    vec1 = [1, 2, 3, 5]
    vec2 = [4, 4, 4, 5]
    assert first_repeated(vec1, vec2) == 5
