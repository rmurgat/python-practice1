
# [source:] https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    def printTree(self):
        print(self.data)

    def insert(self, data):
        return

    def inorderTraversal(self, data):
        return
    
    def preorderTraversal(self, data):
        return
    
    def postorderTraversal(self, data):
        return

class btree1:

    def print_InOrderTraversal():
        return

    def menu(self):
        while True:
            print("[ B-TREE MAIN MENU ]")
            print("1. In-order Traversal B-Tree")
            print("2. Pre-order Traversal B-Tree")
            print("3. Post-order Traversal B-Tree")
            print("99. Exit")
            x = int(input("enter you option? "))
            if x==1: self.print_InOrderTraversal()
            if x==99: return

app = btree1()
app.menu()            
