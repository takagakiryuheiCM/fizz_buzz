from typing import Literal

FizzBuzzOutput = Literal["Fizz"] | Literal["Buzz"] | Literal["FizzBuzz"]

def fizz_buzz(number: int) -> FizzBuzzOutput | int:
    if not 1 <= number <= 100:
        raise ValueError("1~100の間の数値を指定してください")

    is_fizz_num = number % 3 == 0
    is_buzz_num = number % 5 == 0
    
    if is_fizz_num and is_buzz_num:
        return "FizzBuzz"
    elif is_fizz_num:
        return "Fizz"
    elif is_buzz_num:
        return "Buzz"
    else:
        return number

if __name__ == "__main__":
    for i in range(1, 101):
        print(fizz_buzz(i))
