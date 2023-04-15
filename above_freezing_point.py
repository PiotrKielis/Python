from abc import ABC, abstractmethod

class Temperature(ABC):
    def __init__(self, temperature):
        self._temperature = temperature

    @property
    @abstractmethod
    def temperature(self):
        pass

    @temperature.setter
    @abstractmethod
    def temperature(self, value):
        pass

    def __str__(self):
        return f"{self.temperature} degrees in scale {self.__class__.__name__}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.temperature})"

    def above_freezing(self):
        return self.temperature > 0

    @abstractmethod
    def convert_to_Fahrenheit(self):
        pass

    @abstractmethod
    def convert_to_Celsius(self):
        pass

    @abstractmethod
    def convert_to_Kelvin(self):
        pass


class Fahrenheit(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def convert_to_Fahrenheit(self):
        return self

    def convert_to_Celsius(self):
        celsius = (self.temperature - 32) * 5/9
        return Celsius(celsius)

    def convert_to_Kelvin(self):
        celsius = self.convert_to_Celsius().temperature
        kelvin = celsius + 273.16
        return Kelvin(kelvin)


class Celsius(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def convert_to_Fahrenheit(self):
        fahrenheit = (self.temperature * 9/5) + 32
        return Fahrenheit(fahrenheit)

    def convert_to_Celsius(self):
        return self

    def convert_to_Kelvin(self):
        kelvin = self.temperature + 273.16
        return Kelvin(kelvin)


class Kelvin(Temperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    @property
    def temperature(self):
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        self._temperature = value

    def convert_to_Fahrenheit(self):
        celsius = self.temperature - 273.16
        fahrenheit = (celsius * 9/5) + 32
        return Fahrenheit(fahrenheit)

    def convert_to_Celsius(self):
        celsius = self.temperature - 273.16
        return Celsius(celsius)

    def convert_to_Kelvin(self):
        return self



temperatures = [
    Fahrenheit(32), Fahrenheit(68), Fahrenheit(104), Fahrenheit(140),
    Celsius(-10), Celsius(0), Celsius(20), Celsius(30),
    Kelvin(240), Kelvin(273.16), Kelvin(293.16), Kelvin(310)
]
for temp in temperatures:
    print(temp)
    print(f"{temp.convert_to_Fahrenheit()}")
    print(f"{temp.convert_to_Celsius()}")
    print(f"{temp.convert_to_Kelvin()}")
    print(f"Above freezing point: {temp.above_freezing()}")
    print()
