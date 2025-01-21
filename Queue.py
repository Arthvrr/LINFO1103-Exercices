"""
Complexité amortie de enqueue en ϴ(1)
Complexité de enqueue en ϴ(N) si débordement
Complexité de dequeue en ϴ(1)

STACK ==> LIFO
QUEUE ==> FIFO

Ajout d'un élément à la fin de la liste
Suppression d'un élément en début de liste
"""

class Queue:

    def __init__(self):
        self.liste = []

    def __len__(self):
        return len(self.liste)

    def enqueue(self, item):
        self.liste.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        else:
            elem = self.liste[0]
            self.liste.pop(0)
            return elem

    def is_empty(self):
        return len(self) == 0

    def __str__(self):
        return str(self.liste)
    

queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue)

while (len(queue) > 0):
    queue.dequeue()
    print(queue)