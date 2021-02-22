def test_calc_y():
    from find_y import calc_y
    point_1 = (1,1)
    point_2 = (2,2)
    x_of_point_3 = 0
    expected_result = 0
    result = calc_y(point_1, point_2, x_of_point_3)
    assert result == expected_result

def test_calc_m():
    from find_y import calc_m
    x1 = 1
    y1 = 1
    x2 = 2
    y2 = 2 
    expected_result = 1
    result = calc_m(x1, y1, x2, y2)
    assert result == expected_result


def test_calc_y_int():
    from find_y import calc_y_int
    x1 = 1
    y1 = 1
    m = 1
    expected_result = 0
    result = calc_y_int(x1,y1,m)
    assert result == expected_result

def test_convert_input(x1, y1, x2, y2):
    from find_y import convert_input
    x1 = "1"
    y1 = "1"
    x2 = "2"
    y2 = "2"
    expected_result1 = (1, 1)
    expected_result2 = (2, 2)
    (result1, result2) = convert_input(x1, y1, x2, y2)
    assert result1 == expected_result1
    assert result2 == expected_result2
    