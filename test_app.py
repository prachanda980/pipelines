import pytest
from .app import  sum_two_numbers, multiply_two_numbers, subtract_two_numbers, divide_two_numbers, power_two_numbers, modulus_two_numbers
class TestApp:
    def test_add(self):
        assert sum_two_numbers(2, 3) == 5
        assert sum_two_numbers(-1, 1) == 0

    def test_subtract(self):
        assert subtract_two_numbers(5, 3) == 2
        assert subtract_two_numbers(0, 0) == 0

    def test_multiply(self):
        assert multiply_two_numbers(4, 5) == 20
        assert multiply_two_numbers(-1, 1) == -1
    def test_divide(self):
        assert divide_two_numbers(10, 2) == 5
        with pytest.raises(ValueError):
            divide_two_numbers(5, 0)    

    def test_power(self):
        assert power_two_numbers(2, 3) == 8
        assert power_two_numbers(5, 0) == 1
    def test_modulus(self):
        assert modulus_two_numbers(10, 3) == 1
        assert modulus_two_numbers(5, 5) == 0

    


