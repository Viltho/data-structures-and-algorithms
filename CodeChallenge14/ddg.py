def duckduckgoose(arr, k):
    count, indx = 0, 0
    while len(arr) > 1:
        count += 1
        print(arr, count, indx)
        if count == k:
            print(f"{arr[indx]} has been removed")
            arr.pop(indx)
            count = 0
            indx -= 1
        indx = (indx + 1) % len(arr)

    return f"{arr[0]} is the one remaining"

print(duckduckgoose(["a","b","c","d","e","f"], 3))


# 0    >> 0 + 1 % 7 >> 1
# 1    >> 1 + 1 % 7 >> 2
# ...
# 6    >> 6 + 1 % 7 >> 0

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        self.max = 0

    counter = 0

    def insert(self, value):
        LinkedList.counter += 1
        node = Node(value)
        node.next = self.head
        self.head = node
        if node.value > self.max:
            self.max = node.value


ll1 = LinkedList()
ll1.insert(1)
ll1.insert(2)
ll1.insert(8)
ll1.insert(4)
ll1.insert(3)
ll1.insert(23)

print(ll1.max)

        
        
        