import numpy
import array


def cratingInts():
    num = int()
    print("Integer value:", num)

def creatingArrays():
    my_array = array.array('i',[1,2,3,4,5])
    print("METHOD 1: Using array library: The new created array is: ", end="")
    my_array.append(6)
    for i in range(len(my_array)):
        print(my_array[i], end=", ")
    print()

    print("METHOD 2: Using numpy library: ", end="")
    my_array2 = numpy.array([1,2,3,4,5,6,7,8],dtype=int)
    my_array2 = numpy.append(my_array2,[9])
    print("numpy.myarray2 dType:", my_array2.dtype)
    for i in my_array2:
        print(i, end=", ")
    print()

def convertingStringNumbers2FloatList():
    floatNum = float()
    numStr = "10,20,30,40,50,60,70,80,90,100"
    print("Write a Python program to convert these numbers into string then into float types")
    numbers = numStr.split(",")
    numsFloat1 = [float(num) for num in numbers]
    numsFloat1.append("Ruben Murga")
    print("METHOD #1: floatNum:", floatNum, " List numbers in float: ", numsFloat1)
    numsFloat2 = list(map(float,numbers))
    numsFloat2.append("Ruben Murga")    
    print("METHOD #2: List numbers in float (using map()): ", numsFloat2)
    numsFloat3 = numpy.array(numbers,dtype=float)
    # numsFloat3.add("Ruben Murga")  - cannot add String to Float array  
    print("METHOD #3: List numbers in float (using numpy lib): ", numsFloat3)

def playingList():
    lst = [1,2,3,4,5,6,8,9,10]
    print("len()", len(lst))
    print("max():", max(lst))
    print("min():", min(lst))
    print("sum():", sum(lst))


def main():

    while True:
        print("[ MAIN MENU ]")
        print("1. playing with int numbers")
        print("2. playing with arrays")
        print("3. converting String numbers into float list")
        print("4. playing with List")
        print("5. playing with Tuples")
        print("99. to Exit")
        print("Type option:")
        x = int(input())
        match x:
            case 1: cratingInts()
            case 2: creatingArrays()
            case 3: convertingStringNumbers2FloatList()
            case 4: playingList()
            case 99: return
            case _: print("Invalid Option")

main()