"""
Complexité amortie de enqueue en ϴ(1)
Complexité de enqueue en ϴ(N) si débordement
Complexité de dequeue en ϴ(1)

STACK ==> LIFO
QUEUE ==> FIFO

Ajout d'un élément en fin de liste
Suppression d'un élément en fin de liste
"""

class Stack:
    
    def __init__(self):
        self.liste = []

    def __len__(self):
        return len(self.liste)

    def push(self, item):
        self.liste.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.liste.pop()

    def is_empty(self):
        return len(self) == 0

    def __str__(self):
        return str(self.liste)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)

print(stack)

while len(stack) > 0:
    stack.pop()
    print(stack)
