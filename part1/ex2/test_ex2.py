from part1.ex2.ex2 import find_file
import platform


def test_find_file():
    """
    Test verifies whether
    """
    if platform.system() == "Windows":
        assert 'C:\\' == find_file(path='C:\\')
    elif platform.system() == "Linux":
        assert '/proc' == find_file(path='/proc')
    else:  # no support for other platforms
        assert False
