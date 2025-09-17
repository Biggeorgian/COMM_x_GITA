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

try:
    temp = Temperature(32)
    print(f"1 მონაცემი:  {temp.celsius}°C უდრის {temp.fahrenheit:.2f}°F")

    temp = Temperature(-7)
    print(f"2 მონაცემი: {temp.celsius}°C უდრის {temp.fahrenheit:.2f}°F")

    temp = Temperature(-273.15)
    print(f"3 მონაცემი: {temp.celsius}°C უდრის {temp.fahrenheit:.2f}°F")

    temp = Temperature(-700)
    print(f"4 მონაცემი: {temp.celsius}°C უდრის {temp.fahrenheit:.2f}°F")
except ValueError as message:
    print(f"❌ დაფიქსირდა შეცდომა: {message}")