import math
import abc

class Cosmic_object(abc.ABC):
    def __init__(self, name, mass, radius, gravity, water, r_speed):
        self._name = name
        self.__mass = mass
        self.__radius = radius
        self.__gravity = gravity
        self.__water = water
        self.__r_speed = r_speed

    @property
    def name(self):
        return self._name

    def daylength(self):
        ecuatorial_length = 2 * math.pi * (self.__radius * 1000)  # მეტრებში
        period_seconds = ecuatorial_length / self.__r_speed
        return period_seconds / 3600

    def possibility_of_life(self):
        if self.__water:
            return f"წყალი არის. სიცოცხლე შესაძლებელია."
        else:
            return f"ზედაპირზე წყალი არ არის. სავარაუდოდ სიცოცხლე შეუძლებელია"

    def gravity(self):
        return self.__gravity / 9.8


    @abc.abstractmethod
    def get_description(self):
        pass

class Atmosphere:
    def __init__(self, composition):
        self.composition = composition

    def get_atmosphere_info(self):
        return f"ატმოსფეროს შემადგენლობა: {', '.join(self.composition)}."

# პოლიმორფიზმი
class Mars(Cosmic_object):
    def __init__(self):
        super().__init__(
            name="მარსი", mass="6.42e23 კგ", radius=3389, water=False,
            gravity=3.71, r_speed=241
        )

    def get_description(self):
        return (f"{self.name} - წითელი პლანეტა. "
                f"დღე-ღამის ხანგრძლივობა: {self.daylength():.2f} საათი.\n"
                f"{self.possibility_of_life()}\n"
                f"ფარდობითი გრავიტაცია დედამიწასთან: {self.gravity():.2f}")

class Moon(Cosmic_object):
    def __init__(self):
        super().__init__(
            name="მთვარე", mass="7.34e22 კგ", radius=1737, water=False,
            gravity=1.62, r_speed=4.6
        )

    def daylength(self):
        return 709

    def get_description(self):
        return (f"{self.name} - დედამიწის ბუნებრივი თანამგზავრი. "
                f"დღე-ღამე: {self.daylength()} საათი.\n"
                f"{self.possibility_of_life()}\n")

# მრავალჯერადი მემკვიდრეობა
class Earth(Cosmic_object, Atmosphere):
    def __init__(self):
        Cosmic_object.__init__(
            self, name="დედამიწა", water=True, gravity=9.8, mass="5.972e24 კგ",
            radius=6371, r_speed=460
        )
        Atmosphere.__init__(self, composition=["ჟანგბაადი", "ნახშირორჟანგი", "აზოტი"])

    # --- პრინციპი 2: პოლიმორფიზმი ---
    def get_description(self):
        return (f"{self.name} - ადმიანების მშობლიური პლანეტა. "
                f"დღე-ღამის ხანგრძლივობა: {self.daylength():.2f} საათი.\n"
                f"{self.possibility_of_life()}\n"
                f"{self.get_atmosphere_info()}\n")

bodies = [Earth(), Moon(), Mars()]
for body in bodies:
    print(body.get_description())