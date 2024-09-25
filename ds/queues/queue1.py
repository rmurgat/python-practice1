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

def playingQueueCollection():
    queue = Queue()

    queue.enqueue("Alberto")
    queue.enqueue("Boriqua")
    queue.enqueue("Camisiano")
    queue.enqueue("David")
    queue.enqueue("Ernesto")

    print("printing original queue: ", queue)
    print("printing dequeue(): ", queue.dequeue())
    print("printing after dequeue: ", queue)

def main():
    while True:
        print("MAIN MENU")
        print("1. playing Queue using collection")
        print("2. playing Priority Queue")
        print("99. to Exit")
        print("Type option:")
        x = int(input())
        match x:
            case 1: playingQueueCollection()
            case 2: print("option 2, selected")
            case 99: exit(0)
            case _: print("Invalid Option")

main()


