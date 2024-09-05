from collections import deque 

class StackDequeue:
    def __init__(self):
        self._elements = deque()

    def push(self, element):
        self._elements.append(element)

    def pop(self):
        return self._elements.pop()
    
    def __str__(self) -> str:
        res = ""
        for i in self._elements:
            res = res + i + ", "
        return "[" + res + "]"

class MyStack:
    MAX = 10
    stack = [0] * MAX
    top = -1 

    def __init__(self) -> None:
        pass

    def push(self, val):
        if self.isFull():
            print('Stack is Full')
            return
        self.top = self.top + 1
        #print('push().top: ', self.top)
        self.stack[self.top]=val
        
    def pop(self):
        if self.isEmpty():
            print('Stack is Empty')
            return
        res = self.stack[self.top]
        self.top= self.top - 1
        #print('pop().top: ', self.top)
        return res
        
    def isFull(self):
        if self.top==(self.MAX-1):
            return True
        return False
    
    def isEmpty(self):
        if self.top<0:
            return True
        return False
    
    def len(self):
        return len(self.stack)

    def __str__(self):
        s = "";
        try:
            for index in range(self.top+1):
                s = s + str(self.stack[index]) + ", ";
        except Exception as e:
            s="Exception"
        return "[" + s + "]"
    

def playingStacks():
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    print('.PLAYING WITH MY OWN STACK.')   
    print(stack)

    print('pop: ', stack.pop())
    print('pop: ', stack.pop())
    print('Minus 2: ', stack)
    print('pop: ', stack.pop())
    print('pop: ', stack.pop())
    print('Minus 4: ', stack)
    print('pop: ', stack.pop())
    print('pop: ', stack.pop())
    print('Minus 6: ', stack)

def playingEmptyStack():
    print('.PLAYING WITH MY OWN EMPTY STACK.')    
    myEmptyStack = MyStack()
    print('printing empty stack: ', myEmptyStack)
    myEmptyStack.push(1)
    myEmptyStack.push(2)
    myEmptyStack.push(3)
    myEmptyStack.push(4)
    print('printing stack: ', myEmptyStack)
    myEmptyStack.pop()
    myEmptyStack.pop()
    myEmptyStack.pop()
    myEmptyStack.pop()
    myEmptyStack.pop()
    print('printing pops() stack: ', myEmptyStack)

def playingWithList():
    print('.PLAYING STACKS WITH LIST.') 
    mystack = []

    mystack.append('Juan')
    mystack.append('Pablo')
    mystack.append('II')
    mystack.append('Papa')
    mystack.append('Churck')
    mystack.append('Catholic')

    print('printing stack: ', mystack)

    popstr = mystack.pop()
    print('printing stack.pop(): ', popstr)
    print('printing stack after pop(): ', mystack)

def playingWithStackDequeue():
    stack = StackDequeue()

    stack.push('Fredy')
    stack.push('Javier')
    stack.push('Fernando')
    stack.push('Lazaro')
    print('printing original stack: ', stack)
    popresult = stack.pop()
    print('printing stack after pop(): ', popresult)
    print(stack)   

def main():
    

    while True:
        print("MAIN MENU")
        print("1. Stack program in Python")
        print("2. Dealing with Empty Stack")
        print("3. Stack using Python List")
        print("4. Stack using Collections.dequeue")
        print("99. to Exit")
        print("Type option:")
        x = int(input())
        match x:
            case 1: playingStacks()
            case 2: playingEmptyStack()
            case 3: playingWithList()
            case 4: playingWithStackDequeue()
            case 99: return
            case _: print("Invalid Option")

main()
