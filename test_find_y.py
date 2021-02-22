import pytest

@pytest.mark.parametrize("input1, input2, input3, expected", [
    ((1, 1), (2, 2), 0, 0),
    ((2, 5), (4, 1), 1, 7)
])
def test_calc_y(input1, input2, input3, expected):
    from find_y import calc_y
    result = calc_y(input1, input2, input3)
    assert result == expected

@pytest.mark.parametrize("input1, input2, input3, input4, expected", [
    (1, 1, 2, 2, 1),
    (2, 5, 4, 1, -2)
])
def test_calc_m(input1, input2, input3, input4, expected):
    from find_y import calc_m
    result = calc_m(input1, input2, input3, input4)
    assert result == expected

@pytest.mark.parametrize("input1, input2, input3, expected", [
    (1, 1, 1, 0),
    (2, 5, -2, 9)
])
def test_calc_y_int(input1, input2, input3, expected):
    from find_y import calc_y_int
    result = calc_y_int(input1, input2, input3)
    assert result == expected


@pytest.mark.parametrize("input1, input2, input3, input4, input5, expected1, expected2, expected3", [
    ("1","1","2","2","1",(1,1),(2,2),1),
    ("2","5","4","1","1",(2,5),(4,1),1)
])
def test_convert_input(input1, input2, input3, input4, input5, expected1, expected2, expected3):
    from find_y import convert_input
    (result1, result2, result3) = convert_input(input1, input2, input3, input4, input5)
    assert result1 == expected1
    assert result2 == expected2
    assert result3 == expected3

    