from abc import ABC, abstractmethod

# Membuat interface 'Plumber'
class Plumber(ABC):
    @abstractmethod
    def unplugDrain(self):
        pass

# Membuat interface 'Electrician'
class Electrician(ABC):
    @abstractmethod
    def changeBulb(self):
        pass

# Class 'Human' sebagai base class
class Human:
    def __init__(self, name):
        self.name = name

    def toString(self):
        return f"Name: {self.name}"

# Subclass 'HandyPerson' yang menggabungkan Plumber, Human, dan Electrician
class HandyPerson(Plumber, Human, Electrician):
    def changeBulb(self):
        return f"{self.name} is changing a light bulb."

    def unplugDrain(self):
        return f"{self.name} is unplugging a drain."

    def toString(self):
        return f"HandyPerson: {self.name}"

# Subclass 'IndustrialPlumber' yang menggabungkan Plumber dan Human
class IndustrialPlumber(Plumber, Human):
    def unplugDrain(self):
        return f"{self.name} is unplugging an industrial drain."

# Subclass 'NobodySpecial' yang menggabungkan Human
class NobodySpecial(Human):
    def toString(self):
        return f"NobodySpecial: {self.name}"

# Contoh penggunaan:
if __name__ == "__main__":
    handy_person = HandyPerson("Farrel")
    industrial_plumber = IndustrialPlumber("Yosan")
    nobody_special = NobodySpecial("Navyansyah")

    print(handy_person.toString())
    print(handy_person.changeBulb())
    print(handy_person.unplugDrain())

    print(industrial_plumber.toString())
    print(industrial_plumber.unplugDrain())

    print(nobody_special.toString())