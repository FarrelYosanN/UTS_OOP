from abc import ABC, abstractmethod

# Membuat interface 'Tossable'
class Tossable(ABC):
    @abstractmethod
    def toss(self):
        pass

# Subclass 'Ball' yang mengimplementasikan interface 'Tossable'
class Ball(Tossable):
    def __init__(self, brandName):
        self.brandName = brandName

    def getBrandName(self):
        return self.brandName

    def toss(self):
        print(f"{self.brandName} ball has been tossed.")

    def bounce(self):
        print(f"{self.brandName} ball is bouncing.")

# Subclass 'Rock' yang juga mengimplementasikan interface 'Tossable'
class Rock(Tossable):
    def toss(self):
        print("Rock has been tossed.")

# Subclass 'Baseball' yang merupakan subclass dari 'Ball'
class Baseball(Ball):
    def __init__(self, brandName):
        super().__init__(brandName)

    def bounce(self):
        print(f"{self.brandName} baseball is bouncing.")

# Subclass 'Football' yang juga merupakan subclass dari 'Ball'
class Football(Ball):
    def __init__(self, brandName):
        super().__init__(brandName)

    def bounce(self):
        print(f"{self.brandName} football is bouncing.")

# Contoh penggunaan:
if __name__ == "__main__":
    baseball = Baseball("Wilson")
    football = Football("Adidas")
    rock = Rock()

    print(f"\nBaseball brand: {baseball.getBrandName()}")
    baseball.toss()
    baseball.bounce()

    print(f"\nFootball brand: {football.getBrandName()}")
    football.toss()
    football.bounce()

    print("\nRock:")
    rock.toss()