from typing import Literal

def fizz_buzz(number: int) -> str:
    if not 1 <= number <= 100:
        raise ValueError(f"1~100の間の数値を指定してください。不正な数値: {number}")

    is_fizz_num = number % 3 == 0
    is_buzz_num = number % 5 == 0
    
    if is_fizz_num and is_buzz_num:
        return "FizzBuzz"
    elif is_fizz_num:
        return "Fizz"
    elif is_buzz_num:
        return "Buzz"
    else:
        return str(number)
    
def fizz_buzz_list(start: int, end: int) -> list[str]:
    return [fizz_buzz(n) for n in range(start, end + 1)]

if __name__ == "__main__":
    print('\n'.join(fizz_buzz_list(1, 100)))

    # for i in range(1, 101):
    #     print(fizz_buzz(i))
