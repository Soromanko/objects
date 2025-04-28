class Dog:
    # name = "Vlčák"
    # weight = 5

    def __init__(self, jmeno, vaha):
        self.name = jmeno
        self.weight = vaha

    def say_hello(self):
        print(f"Ahoj, já jsem {self.name} a mám {self.weight}kg")

dog = Dog("Alík", 1)
dog2 = Dog("Hafík", 4)

dog.say_hello()
dog2.say_hello()
#print(f"Jméno: {dog.name} a váha: {dog.weight}kg")
#print(f"Jméno: {dog2.name} a váha: {dog2.weight}kg")