'''
The exercise consists in implementing the three following problems in Python as
parameterized functions. Also, add at least 2 unit tests for each function to verify that the
implementation works as expected. Use a testing framework (for example PyTest)
1. A function that given 2 vectors of integers finds the first repeated number
2. A function that given a path of the file system finds the first file that meets the
following requirements
a. The file owner is admin
b. The file is executable
c. The file has a size lower than 14*2^20
3. A function that given a sequence of coin flips (0 is tails, 1 is heads) finds the
minimum quantity of permutations so that the sequence ends interspersed. For
example, given the sequence 0,1,1,0 how many changes are needed so that the
result is 0,1,0,1
'''

from typing import List
import itertools


def first_repeated(vec1: List[int], vec2: List[int]):
    """
    1. A function that given 2 vectors of integers finds the first repeated number
    :param vec1: list of integers
    :param vec2: list of integers
    :return: Function returns first repeated number between two vectors on the same index.
            Function returns -1 in case there is no repeated number
    """
    if len(vec1) == 0 or len(vec2) == 0:
        raise BaseException("Lenght of vector is 0")
    if type(vec1) != list or type(vec2) != list:
        raise TypeError("Wrong data type")
    if not all(isinstance(x, int) for x in vec1):
        raise TypeError("Not all elements in vector type int")
    if not all(isinstance(x, int) for x in vec2):
        raise TypeError("Not all elements in vector type int")

    for elem1,elem2 in itertools.zip_longest(vec1, vec2):
        if elem1==elem2:
            return elem1
    return -1
