from fizz_buzz import fizz_buzz

def test_fizz_buzz_for_range_1_to_100():
    for i in range(1, 101):
        is_fizz_num = i % 3 == 0
        is_buzz_num = i % 5 == 0

        if is_fizz_num and is_buzz_num:
            assert fizz_buzz(i) == "FizzBuzz"
        elif is_fizz_num:
            assert fizz_buzz(i) == "Fizz"
        elif is_buzz_num:
            assert fizz_buzz(i) == "Buzz"
        else:
            assert fizz_buzz(i) == i

