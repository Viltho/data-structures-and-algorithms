class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    counter = 0

    def insert(self, value):
        LinkedList.counter += 1
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        if self.head is None:
            return False
        else:
            current = self.head
            while(current):
                if current.value == value:
                    return True
                current = current.next
    
    def append(self, value):
        LinkedList.counter += 1
        node = Node(value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while(current.next):
                current = current.next
            current.next = node

    def insert_before(self, value, new_value):
        LinkedList.counter += 1
        node = Node(new_value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            previous = None
            while(current):
                if current.value == value:
                    node.next = current
                    if previous:
                        previous.next = node
                    else:
                        self.head = node
                    break
                else:
                    previous = current
                    current = current.next
    
    def insert_after(self, value, new_value):
        LinkedList.counter += 1
        node = Node(new_value)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while(current):
                if current.value == value:
                    node.next = current.next
                    current.next = node
                    break
                else:
                    current = current.next

    def __str__(self):

        string = ""

        if self.head is None:
            return "This linked list is empty"
        else:
            current = self.head
            while(current):
                string += "{ " + f"{str(current.value)}" + " } -> "
                current = current.next
            
            string = string + "Null"
        return string
