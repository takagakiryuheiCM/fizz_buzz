import pytest
from fizz_buzz import fizz_buzz

def test_fizz_num():
    FIZZ_NUM = 3
    assert fizz_buzz(FIZZ_NUM) == "Fizz"

def test_buzz_num():
    BUZZ_NUM = 5
    assert fizz_buzz(BUZZ_NUM) == "Buzz"

def test_fizz_buzz_num():
    FIZZ_BUZZ_NUM = 15
    assert fizz_buzz(FIZZ_BUZZ_NUM) == "FizzBuzz"

def test_normal_num():
    NORMAL_NUM = 1
    assert fizz_buzz(NORMAL_NUM) == NORMAL_NUM

def test_not_in_range_num():
    NOT_IN_RANGE_NUMBER_FIRST = 101
    NOT_IN_RANGE_NUMBER_SECOND = 0

    with pytest.raises(ValueError) as e:
        fizz_buzz(NOT_IN_RANGE_NUMBER_FIRST)
    assert str(e.value) == "1~100の間の数値を指定してください"

    with pytest.raises(ValueError) as e:
        fizz_buzz(NOT_IN_RANGE_NUMBER_SECOND)
    assert str(e.value) == "1~100の間の数値を指定してください"


