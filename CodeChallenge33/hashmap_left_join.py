class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.value2 = value
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

    def delete(self, value):
        if self.head is None:
            return

        if self.head.value == value:
            self.head = self.head.next
            self.counter -= 1
            return

        current = self.head
        while current.next is not None:
            if current.next.value == value:
                current.next = current.next.next
                self.counter -= 1
                return
            current = current.next

    def kthfromend(self, k):
        if self.head is None:
            return None

        slow = fast = self.head
        for i in range(k):
            if fast is None:
                return None
            fast = fast.next

        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow.value


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
                string += "{ " + f"{str(current.key)} : {str(current.value)} , {str(current.value2)}" + " } -> "
                current = current.next
            
            string = string + "None"
        return string       
        
dict1 = {
    "a": 1,
    "b": 3,
    "c": 2,
    "d": 3,
    "e": 5,
}

dict2 = {
    "b": 3
}
        
def left_join(dict1, dict2):
    """to join dictionary 1 with 2 based on dictionary 1 items, if the items are not available in dictionary 2 return Nulls
    else return the shared values in both dictionary 1 and dictionary 2

    Args:
        dict1 (dictionary): dictionary of items with keys and values
        dict2 (dictionary): dictionary of items with keys and values
    Returns:
        linked list string: after the check shared values in both dictionary 1 and dictionary 2 are pushed into a new data structure, in our case linked list
    """
    linkedlist = LinkedList()
    linkedlist.head = Node("", None)
    current = linkedlist.head
    counter = 0
    
    for key in dict1:
        if key in dict2:
            current.key, current.value, current.value2 = key, dict1[key], dict2[key]
        else:
            current.key, current.value, current.value2 = key, dict1[key], "Null"
            
        counter += 1
        
        if counter == len(dict1):
            break
        
        current.next = Node("", None)
        current = current.next
        
    return str(linkedlist)
