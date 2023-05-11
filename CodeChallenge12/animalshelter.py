from CodeChallenge10.queue import Queue
from CodeChallenge10.node import Cat, Dog
# class Dog:
#     def __init__(self, name):
#         self.name = name
#         self.species = "dog"
# class Cat:
#     def __init__(self, name):
#         self.name = name
#         self.species = "cat"

class AnimalShelter:
    """this is the init for animal shelter where we assign dogs and cats' list"""
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        
    def enqueue(self, animal):
        """this is an enqueue method that takes species from class dog or cat"""
        if animal.species == "dog":
            self.dogs.enqueue(animal.name)
        elif animal.species == "cat":
            self.cats.enqueue(animal.name)
    
    def dequeue(self, pref):
        """this is dequeue for any"""
        if pref == "dog":
            return self.dogs.dequeue()
        elif pref == "cat":
            return self.cats.dequeue()
        else:
            return None

pq1 = AnimalShelter()
dog1 = Dog("Buddy")
# cat1 = Cat("Fluffy")
dog2 = Cat("Max")
# cat2 = Cat("Mittens")
pq1.enqueue(dog1)
# pq1.enqueue(cat1)
pq1.enqueue(dog2)
# pq1.enqueue(cat2)
print(pq1.dogs.dequeue())
# print(pq1.dequeue_dog())
# print(pq1.dequeue("dog"))
# print(pq1.dequeue("cat"))
# print(pq1.dequeue("batar"))
