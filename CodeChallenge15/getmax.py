from CodeChallenge10.node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
        self.max = 0
        self.array_of_nodes = []

    def push(self,value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1
        if self.max == 0:
            self.max = node.value
        elif node.value > self.max:
            self.max = node.value
        self.array_of_nodes.append(node.value)

    def pop(self):
        if self.top is not None:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            if temp.value == self.max:
                
                return temp.value
        else:
            return ("stack is empty")
    
    def getMax(self):
        return self.max
    
    def sort(nums, start=0, end=None):
        print('quicksort', nums, start, end)
        if end is None:
            nums = list(nums)
            end = len(nums) - 1
        
        if start < end:
            pivot = partition(nums, start, end)
            quicksort(nums, start, pivot-1)
            quicksort(nums, pivot+1, end)

        return nums
        
        
    def peek(self):
        if self.top:
            return self.top.value
        else:
            return("this stack is empty")
        
    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0
    
    def __str__(self) -> str:
        string = ""

        if self.top is None:
            return "This linked list is empty"
        else:
            current = self.top
            while(current):
                string += "{ " + f"{str(current.value)}" + " } -> "
                current = current.next
            
            string = string + "Null"
        return string

