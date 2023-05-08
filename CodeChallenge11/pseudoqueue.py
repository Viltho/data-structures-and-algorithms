from CodeChallenge10.stack import Stack

class PseudoQueue:
    def __init__(self):
        # creating 2 stack instances from stack
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        # using stack's methods, here push
        self.stack1.push(value)

    def dequeue(self):
        # using stack's methods, here push and pop
        if self.stack1.top is None and self.stack2.top is None:
            return "This queue stack is empty"
        elif self.stack1.top is not None and self.stack2.top is None:
            while self.stack1.top:
                self.stack2.push(self.stack1.pop())
            return self.stack2.pop()
        elif self.stack1.top is not None and self.stack2.top is not None:
            return self.stack2.pop()

pq1 = PseudoQueue()
pq1.enqueue("A")
pq1.enqueue("B")
pq1.enqueue("C")

print(pq1.dequeue())
print(pq1.stack2)