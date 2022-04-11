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

import os, glob

MAX_FILE_SIZE = 14 * pow(2, 20)


def find_file(path: str):
    """
    2. A function that given a path of the file system finds the first file that meets the following requirements
    a. The file owner is admin
    b. The file is executable
    c. The file has a size lower than 14*2^20 (asuming in bytes)
    :param path: path to file system
    :return: function returns first file that meets requirements specified above. If function does not find a proper file it returns -1
    """
    for file in glob.iglob(path + "**/**", recursive=True):
        st = os.stat(file, follow_symlinks=False)
        executable = os.access(file, os.X_OK)
        if executable and st.st_uid == 0 and st.st_size < MAX_FILE_SIZE:
            return file
    return -1
