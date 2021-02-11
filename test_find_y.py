def test_find_y():
    from find_y import calc_y
    x1 = 1
    y1 = 1
    x2 = 2
    y2 = 2
    x = 0
    expected_result = 0

    result = calc_y(x1, y1, x2, y2, x)

    assert result == expected_result
