class Dog:
    def __init__(self, name):
        self.name = name
        self.species = "dog"
class Cat:
    def __init__(self, name):
        self.name = name
        self.species = "cat"

class AnimalShelter:
    """this is the init for animal shelter where we assign dogs and cats' list"""
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.order = 0
        
    def enqueue(self, animal):
        """this is an enqueue method that takes species from class dog or cat"""
        if animal.species == "dog":
            self.dogs.append((animal.name, self.order))
        elif animal.species == "cat":
            self.cats.append((animal.name, self.order))
        self.order += 1
    
    def dequeue(self, pref):
        """this is dequeue for any"""
        if pref == "dog":
            return self.dogs.pop(0)[0]
        elif pref == "cat":
            return self.cats.pop(0)[0]
        else:
            return None

pq1 = AnimalShelter()
dog1 = Dog("Buddy")
# cat1 = Cat("Fluffy")
dog2 = Dog("Max")
# cat2 = Cat("Mittens")
pq1.enqueue(dog1)
# pq1.enqueue(cat1)
pq1.enqueue(dog2)
# pq1.enqueue(cat2)
print(pq1.dogs)
# print(pq1.dequeue_dog())
# print(pq1.dequeue("dog"))
# print(pq1.dequeue("cat"))
# print(pq1.dequeue("batar"))
