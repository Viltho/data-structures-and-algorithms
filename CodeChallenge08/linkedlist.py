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
                string += "{ " + f"{str(current.value)}" + " } -> "
                current = current.next
            
            string = string + "Null"
        return string
    
def zip_lists(list1, list2):
    if not list1.head or not list2.head:
        return list1 if list1.head else list2

    new_list = LinkedList()
    current1 = list1.head
    current2 = list2.head
    new_list.head = current1

    while current1 and current2:
        temp1 = current1.next
        temp2 = current2.next

        current1.next = current2
        current2.next = temp1

        current1 = temp1
        current2 = temp2
        
    if current2:
        while current2:
            new_list.append(current2.value)
            current2=current2.next

    return new_list