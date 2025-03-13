class Animal:

    details = dict()

    def habitat(self, place):
        self.details['Habitat'] = place

    def size(self, size):
        self.details["Abilities"] = size

    def about(self, comment):
        self.details["About"] = comment

    def danger(self, level):
        self.details["Danger level"] = level

    def __str__(self):
        intext = str()
        for a, b in self.details.items():
            intext = intext + str(a) + ': ' + str(b) + '\n'
        return intext
    
class Bird(Animal):
    def __init__(self):
        Animal.details['Type'] = 'Bird'
    def flight(self, distance):
        self.details["Flying distance"] = distance

class Mammal(Animal):
    def __init__(self):
        Animal.details['Type'] = 'Mammal'
    def cubs(self, number):
        self.details["Number of cubs"] = number

class Fish(Animal):
    def __init__(self):
        Animal.details['Type'] = 'Fish' 
    
elephant = Mammal() 
elephant.habitat("Africa, South Asia")
elephant.size("Very big")
elephant.danger("Mild")
elephant.about("A cute animal, but it is too dangerous if it sees you as danger.")
elephant.cubs('1 or 2')
print(elephant)