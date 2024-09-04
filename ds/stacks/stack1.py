
class Stack:
    MAX = 10
    stack = [0] * 10
    top = 0 

    def __init__(self) -> None:
        pass

    def push(self, val):
        if self.isFull():
            print('Stack is Full')
            return
        self.stack[self.top]=val
        self.top+=1
        
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
            return
        res = self.stack[self.top]
        self.top-=1
        return res
        
    def isFull(self):
        if self.top==self.MAX-1:
            return True
        return False
    
    def isEmpty(self):
        if self.top==0:
            return True
        return False
    def __str__(self):
        s = "";
        for index in range(self.top):
            s = s + str(self.stack[index]) + ", ";
        return "[" + s + "]"

def playingStacks():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print(stack)

    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack)

def main():
    

    while True:
        print("MAIN MENU")
        print("1. Stack program in Python")
        print("99. to Exit")
        print("Type option:")
        x = int(input())
        match x:
            case 1: playingStacks()
            case 99: return
            case _: print("Invalid Option")

main()