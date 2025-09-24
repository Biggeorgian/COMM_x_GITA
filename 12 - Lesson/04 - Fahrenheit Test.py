import pytest

class Temperature:
    zero = -273.15
    def __init__(self, celsius: float):
        self.celsius = celsius

    @property
    def celsius(self):
        return self.__celsius

    @celsius.setter
    def celsius(self, value: float):
        # გამოვრიცხოთ ფიზიკის კანონების დარღვევა
        if value >= self.zero:
            self.__celsius = value
        else:
            raise ValueError (f"ტემპერატურა ვერასდროს დაეცემა "
                              f"აბსოლუტურ ნულზე {self.zero} დაბლა")

    @property
    def fahrenheit(self):
        return (self.celsius * 9 / 5) + 32


def test_celsius_to_fahrenhait():
    temp_freezing = Temperature(0)
    assert temp_freezing.fahrenheit == pytest.approx(32)

    temp_boiling = Temperature(100)
    assert temp_boiling.fahrenheit == pytest.approx(212)

    temp_equal = Temperature(-40)
    assert temp_equal.fahrenheit == pytest.approx(-40)

def test_zero_conversion():
    abs_zero = Temperature(-273.15)
    assert abs_zero.fahrenheit == pytest.approx(-459.67)

def test_below_zero():
    with pytest.raises(ValueError) as excinfo:
        Temperature(-300)
    assert "აბსოლუტურ ნულზე" in str(excinfo.value)

def test_setter_functionality():
    temp = Temperature(20)
    temp.celsius = 25
    assert temp.celsius == 25
    assert temp.fahrenheit == pytest.approx(77)