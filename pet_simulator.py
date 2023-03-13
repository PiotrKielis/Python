import string
class Pet:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3 or not all(c.isalpha()for c in name):
            raise ValueError("Invalid name. Name must be a string with at least 3 alphabetical characters.")
        self.name = name
        self.hunger = 0
        self.tiredness = 0

    def _passage_of_time(self):
        self.hunger += 1
        self.tiredness += 1

    @property
    def mood(self):
        sum_levels = self.hunger + self.tiredness
        if sum_levels < 5:
            return"happy"
        elif sum_levels <= 10:
            return"content"
        elif sum_levels <= 15:
            return"frustrated"
        else:
            return"angry"

    def talk(self):
        self._passage_of_time()
        if self.mood == "happy":
            print(f"{self.name} is happy and content.")
        elif self.mood == "content":
            print(f"{self.name} is feeling alright.")
        elif self.mood == "frustrated":
            print(f"{self.name} is starting to get frustrated.")
        else:
            print(f"{self.name} is very angry!")

    def eat(self, food=4):
        self._passage_of_time()
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0

    def play(self, fun=4):
        self._passage_of_time()
        self.tiredness -= fun
        if self.tiredness < 0:
            self.tiredness = 0

    def __str__(self):
        return f"{self.name}: hunger:{self.hunger}, tiredness:{self.tiredness},mood:{self.mood}"


def main():
    my_pet = Pet("Fluffy")

    print(my_pet)
    my_pet.eat(2)
    my_pet.play(3)
    my_pet.play(1)
    my_pet.eat(1)
    my_pet.play(2)
    print(my_pet)
    my_pet.talk()
    my_pet.eat(6)
    my_pet.play(5)
    print(my_pet)
    my_pet.talk()

main()
