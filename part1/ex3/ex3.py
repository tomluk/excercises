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


def flip_coins(sequence: list):
    """
    3. A function that given a sequence of coin flips (0 is tails, 1 is heads) finds the
    minimum quantity of permutations so that the sequence ends interspersed. For
    example, given the sequence 0,1,1,0 how many changes are needed so that the
    result is 0,1,0,1
    :param sequence: list of 0 and 1
    :return: minimal number of changes needed to get interspersed list of 0 and 1
    """
    if len(sequence) < 2:
        raise BaseException("provided sequence to short")

    sequence_copy = sequence.copy()
    # approach 1: flip the first coin and align others
    sequence[0] = 1 if sequence[0] == 0 else 0

    flip_counter_1 = flip(sequence, flip_counter=1)

    # approach 2: do not flip the first coin and align others
    flip_counter_2 = flip(sequence_copy)

    return min(flip_counter_1, flip_counter_2)


def flip(sequence, flip_counter=0):
    """
    Helper function to flip sequence
    :param sequence: list of 0 and 1
    :param flip_counter: number of fliped coins
    :return:
    """
    for index, elem in enumerate(sequence):
        try:
            if sequence[index + 1] == elem:
                sequence[index + 1] = 1 if elem == 0 else 0
                flip_counter += 1
        except IndexError:
            pass
    return flip_counter
