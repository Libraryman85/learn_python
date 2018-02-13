def test_fizz_buzz_zero():
    expected_result = []
    result = fizz_buzz(0)
    assert expected_result == result


def test_fizz_buzz_one():
    expected_result = ['1']
    result = fizz_buzz(1)
    assert expected_result == result

def test_fizz_buzz_two():
    expected_result = ['1','2']
    result = fizz_buzz(2)
    assert expected_result == result


def test_fizz_buzz_three():
    expected_result = ['1','2','fizz']
    result = fizz_buzz(3)
    assert expected_result == result


def test_fizz_buzz_six():
    expected_result = ['1', '2', 'fizz', '4','buzz','fizz']
    result = fizz_buzz(6)
    assert expected_result == result


from beal_katas.fizz_buzz.fizz_buzz import fizz_buzz
