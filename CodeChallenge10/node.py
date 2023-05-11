class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Dog(Node):
    def __init__(self, name):
        self.name = name
        self.species = "dog"

class Cat(Node):
    def __init__(self, name):
        self.name = name
        self.species = "cat"   