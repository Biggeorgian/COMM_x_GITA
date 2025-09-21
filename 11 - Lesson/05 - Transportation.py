import random
import abc

class Transportation:
    def __init__(self, name, fuel, max_speed, capacity, consumption):
        self._name = name
        self.__fuel = fuel
        self._max_speed = max_speed
        self._capacity = capacity
        self._consumption = consumption

    @property
    def name(self):
        return self._name

    @property
    def fuel(self):
        return self.__fuel

    @abc.abstractmethod
    def move(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass

class Bus(Transportation):
    def __init__(self):
        super().__init__(
            name="ავტობუსი", fuel=360, max_speed=120,
            capacity=48, consumption=25
        )
        self._inefficiency_factor = random.uniform(1.2, 1.5)

    def move(self):
        real_consumption = self._inefficiency_factor * self._consumption
        distance = (self.fuel / real_consumption) * 100
        return distance

    def get_description(self):
        return (f"სატრანსპორტო საშუალება {self.name}. "
                f"მაქსიმალური სიჩქარე: {self._max_speed} კმ/სთ.\n"
                f"შეუძლია {self.move():.2f} კმ-ზე გადაიყვანოს "
                f"{self._capacity} მგზავრი\n")

class Car(Transportation):
    def __init__(self):
        super().__init__(
            name="მსუბუქი ავტომანქანა", fuel=45, max_speed=240,
            capacity=5, consumption=14
        )
        self._inefficiency_factor = random.uniform(1, 1.6)

    def move(self):
        real_consumption = self._inefficiency_factor * self._consumption
        distance = (self.fuel / real_consumption) * 100
        return distance

    def get_description(self):
        return (f"სატრანსპორტო საშუალება {self.name}. "
                f"მაქსიმალური სიჩქარე: {self._max_speed} კმ/სთ.\n"
                f"შეუძლია {self.move():.2f} კმ-ზე გადაიყვანოს "
                f"{self._capacity} მგზავრი\n")

class Bike(Transportation):
    def __init__(self):
        super().__init__(
            name="მოტოციკლეტი", fuel=18, max_speed=240,
            capacity=2, consumption=7
        )
        self._inefficiency_factor = random.uniform(1.1, 1.8)

    def move(self):
        real_consumption = self._inefficiency_factor * self._consumption
        distance = (self.fuel / real_consumption) * 100
        return distance

    def get_description(self):
        return (f"სატრანსპორტო საშუალება {self.name}. "
                f"მაქსიმალური სიჩქარე: {self._max_speed} კმ/სთ.\n"
                f"შეუძლია {self.move():.2f} კმ-ზე გადაიყვანოს "
                f"{self._capacity} მგზავრი\n")

vechicles = [Car(), Bus(), Bike()]
for transport in vechicles:
    print(transport.get_description())