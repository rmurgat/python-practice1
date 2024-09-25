
def main():

    
    

    while True:
        print("MAIN MENU")
        print("1. Stack program in Python")
        print("2. Queue program iin Phyton")
        print("99. to Exit")
        print("Type option:")
        x = int(input())
        match x:
            case 1: print("option 1, selected")
            case 2: print("option 2, selected")
            case 99: return
            case _: print("Invalid Option")

main()