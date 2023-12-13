import pytest
from fizz_buzz import fizz_buzz_list

#　範囲内テスト1
def test_in_range_1_to_15():
    START_NUM = 1
    END_NUM = 15
    EXPECTED_LIST = ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
    assert fizz_buzz_list(START_NUM, END_NUM) == EXPECTED_LIST

# 悩みポイント。境界値を確認したいため、END_NUMが100のパターンのテストケースを下に用意したが、範囲内テストを二つに分けるくらいなら1~100で一つのテストで一気にテストしたほうがいいか？
# でもそうすると用意する1~100までの期待値のリストが大きすぎてなんとなく嫌だ
# 範囲内テスト2
def test_in_range_86_to_100():
    START_NUM = 86
    END_NUM = 100
    EXPECTED_LIST = ['86', 'Fizz', '88', '89', 'FizzBuzz', '91', '92', 'Fizz', '94', 'Buzz', 'Fizz', '97', '98', 'Fizz', 'Buzz']
    assert fizz_buzz_list(START_NUM, END_NUM) == EXPECTED_LIST

# 範囲外テスト1
def test_start_num_out_of_range():
    WRONG_START_NUM = 0
    END_NUM = 100
    with pytest.raises(ValueError) as e:
        fizz_buzz_list(WRONG_START_NUM, END_NUM)
    assert str(e.value) == f"1~100の間の数値を指定してください。不正な数値: {WRONG_START_NUM}"

# 範囲外テスト2
def test_end_num_out_of_range():
    START_NUM = 1
    WRONG_END_NUM = 101
    with pytest.raises(ValueError) as e:
        fizz_buzz_list(START_NUM, WRONG_END_NUM)
    assert str(e.value) == f"1~100の間の数値を指定してください。不正な数値: {WRONG_END_NUM}"





