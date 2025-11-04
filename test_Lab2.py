import Lab2

def test_min_max():
    result = []
    input = [3,5,12,2,15]
    test = [2, 15]

    result = Lab2.find_min_max(input)

    assert result == test

def test_average():
    result = 0
    input = [3,5,12,2,15]
    test = 7.4

    result = Lab2.calc_average(input)

    assert result == test
    
def test_median_temperature():
    result = 0
    input = [2,3,5,12,15]
    test = 5

    result = Lab2.calc_median_temperature(input)

    assert result == test