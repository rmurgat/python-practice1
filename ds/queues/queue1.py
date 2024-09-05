from collections import deque

class Queue:
    def __init__(self):
        self._elements = deque()
    def enqueue(self, element):
        self._elements.append(element)
    def dequeue(self):
        return self._elements.popleft()
    def __str__(self) -> str:
        res = ""
        for i in self._elements:
            res = res + i + ", "
        return "[" + res + "]"

queue = Queue()

queue.enqueue('A')
queue.enqueue('B')
queue.enqueue('C')
queue.enqueue('D')
queue.enqueue('E')

print(queue)



