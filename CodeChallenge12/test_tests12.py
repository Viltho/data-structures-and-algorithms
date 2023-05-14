# import pytest

# from CodeChallenge12.animalshelter import AnimalShelter, Dog, Cat

# def test_animal_shelter_enqueue_cat():
#     pq = AnimalShelter()
#     cat1 = Cat("Fluffy")
#     cat2 = Cat("Mittens")
#     pq.enqueue(cat1)
#     pq.enqueue(cat2)
#     expected = "[('Fluffy', 0), ('Mittens', 1)]"
#     actual = str(pq.cats)
#     assert actual == expected

# def test_animal_shelter_enqueue_dog():
#     pq = AnimalShelter()
#     cat1 = Cat("Fluffy")
#     cat2 = Cat("Mittens")
#     pq.enqueue(cat1)
#     pq.enqueue(cat2)
#     expected = "Fluffy"
#     actual = pq.dequeue("cat")
#     assert actual == expected

# def test_animal_shelter_dequeue_cat():
#     pq = AnimalShelter()
#     dog1 = Dog("Buddy")
#     dog2 = Dog("The Big Black")
#     pq.enqueue(dog1)
#     pq.enqueue(dog2)
#     expected = "Buddy"
#     actual = pq.dequeue("dog")
#     assert actual == expected

# def test_animal_shelter_dequeue_dog():
#     pq = AnimalShelter()
#     dog1 = Dog("Buddy")
#     dog2 = Dog("The Big Black")
#     pq.enqueue(dog1)
#     pq.enqueue(dog2)
#     expected = "Buddy"
#     actual = pq.dequeue("dog")
#     assert actual == expected

# def test_animal_shelter_dequeue_any():
#     pq = AnimalShelter()
#     dog1 = Dog("Buddy")
#     dog2 = Dog("The Big Black")
#     pq.enqueue(dog1)
#     pq.enqueue(dog2)
#     expected = None
#     actual = pq.dequeue("any")
#     assert actual == expected