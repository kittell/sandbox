'''
Created on Aug 13, 2020

@author: Kirk Kittell
'''

import pytest

def fizzbuzz(value):
    if is_multiple(value, 3) and is_multiple(value, 5):
        return "FizzBuzz"
    elif is_multiple(value, 3):
        return "Fizz"
    elif is_multiple(value, 5):
        return "Buzz"
    else:
        return str(value)


def is_multiple(value, mod):
    result = (value % mod) == 0
    return result


def check_fizzbuzz(value, expected_value):
    result = fizzbuzz(value)
    assert result == expected_value
    return


def test_return_1_from_1():
    check_fizzbuzz(1, "1")
    return


def test_return_2_from_2():
    check_fizzbuzz(2, "2")
    return


def test_return_fizz_from_3():
    check_fizzbuzz(3, "Fizz")
    return


def test_return_buzz_from_5():
    check_fizzbuzz(5, "Buzz")
    return


def test_return_fizz_from_6():
    check_fizzbuzz(6, "Fizz")
    return


def test_return_buzz_from_10():
    check_fizzbuzz(10, "Buzz")
    return


def test_return_fizzbuzz_from_15():
    check_fizzbuzz(15, "FizzBuzz")
    return