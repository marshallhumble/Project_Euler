# /usr/bin/env python

import time
start = time.time()


"""
Smallest multiple

Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


check_list = [11, 13, 14, 16, 17, 18, 19, 20]


def find_solution(step):
    for num in range(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

def test_function():
    assert find_solution(20) == 232792560


if __name__ == '__main__':
    test_function()

