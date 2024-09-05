from stack1 import Stack

def towerOfHanoi(n, from_rod, to_rod, aux_rod):
    if from_rod.isEmpty() : return
    towerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    towerOfHanoi(n-1, aux_rod, to_rod, from_rod)

def showHanoiRecursion():
    N = 4   # Driver code
    print('.[ SHOW HANOI RECURSION].', N, 'Disks')

    # A, C, B are the name of rods
    towerOfHanoi(N, 'A', 'C', 'B')

def towerOfHanoiStacks(n, from_rod, to_rod, aux_rod):
    if n == 0: return
    towerOfHanoiStacks(n-1, from_rod, aux_rod, to_rod)
    moveDisk(from_rod, to_rod)
    towerOfHanoiStacks(n-1, aux_rod, to_rod, from_rod)

def moveDisk(fromRod, toRod):
    disk = fromRod.pop()
    toRod.append(disk)

def showHanoiUsingStacksAndRecursion():
    origin = []
    target = []
    buffer = []
    origin.append(1)
    origin.append(2)
    origin.append(3)
    print('.[SHOW HANOI USING STACK AND RECURSION].')
    print('origin: ', origin)
    print('processing hanoi...')
    towerOfHanoiStacks(3, origin, target, buffer)
    print('\n[results:]\n')
    print('origin:', origin)
    print('target:', target)
    print('buffer:', buffer)

def main():
    
    while True:
        print(" [ MAIN MENU ] ")
        print("1. Show Hanoi recursion")
        print("2. Show Hanoi using Stack")
        print("99. to Exit")
        print("Type option:")
        x = int(input())
        match x:
            case 1: showHanoiRecursion()
            case 2: showHanoiUsingStacksAndRecursion()
            case 99: return
            case _: print("Invalid Option")

main()