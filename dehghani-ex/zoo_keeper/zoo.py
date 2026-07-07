class Animal:
    zoo_name = 'some zoo'
    def __init__(self,name, species, age, sound, zoo = None):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound
        Animal.zoo_name = zoo

    def make_sound(self):
        print(self.sound)

    def info(self):
        print(self.name, self.species, self.age, self.sound, Animal.zoo_name)

    def __str__(self):
        return f'{self.__dict__}'

class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span

    def make_sound(self):
        pass


lion = Animal('lion', 'cat', 20, 'roaring')
lion.make_sound()
lion.info()

ghanari = Bird('ghanari', 'bird', 1, 'jik-jik', 12)
ghanari.make_sound()
ghanari.info()
print(ghanari)