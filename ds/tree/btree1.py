
# [source:] https://www.tutorialspoint.com/python_data_structure/python_binary_tree.htm
class Node:

    def __init__(self, data:int):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data:int):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
        return

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()


    def prettyTree(self, level=0, side=""):
       ret = "\t"*level+repr(self.data)+" "+side+"\n"
       if self.left: ret += self.left.prettyTree(level+1,"l")
       if self.right: ret += self.right.prettyTree(level+1, "r") 
       return ret        

    def prettyTree2(self, last=True, header=''):
       elbow = "└──"
       pipe = "│  "
       tee = "├──"
       blank = "   "
       print(header + (elbow if last else tee) + str(self.data))
       if self.left: self.left.prettyTree2(last=False if self.right else True, header=header + (blank if last else pipe) )
       if self.right: self.right.prettyTree2(last=True, header=header + (blank if last else pipe))
    
    def inorderTraversal(self, mynode) -> list: 
        res = []
        if mynode:
            res = self.inorderTraversal(mynode.left)
            res.append(mynode.data)
            res = res + self.inorderTraversal(mynode.right)
        return res
    
    def preorderTraversal(self, mynode) -> list:
        res = []
        if mynode:
            res.append(mynode.data)
            res = res + self.preorderTraversal(mynode.left)
            res = res + self.preorderTraversal(mynode.right)
        return res
    
    def postorderTraversal(self, mynode) -> list:
        res = []
        if mynode:
            res = self.postorderTraversal(mynode.left)
            res = res + self.postorderTraversal(mynode.right)
            res.append(mynode.data)
        return res

class btree1:

    def print_OrderTraversal(self):
        root = Node(27)
        root.insert(14)
        root.insert(35)
        root.insert(10)
        root.insert(19)
        root.insert(31)
        root.insert(42)
        root.insert(99)
        root.insert(85)
        root.insert(14)
        root.insert(1)
        root.insert(26)
        root.insert(33)
        root.insert(39)
        root.insert(67)
        root.insert(72)
        root.insert(85)
        root.insert(91)
        root.insert(66)

        print("In Order Traversal: ", root.inorderTraversal(root))
        print("Pre Order Traversal: ", root.preorderTraversal(root))
        print("Post Order Traversal:\n", root.postorderTraversal(root))
        print("Pretty bTree:\n", root.prettyTree())
        print("Pretty bTree II:\n")
        root.prettyTree2()
        return

    def menu(self):
        while True:
            print("[ B-TREE MAIN MENU ]")
            print("1. printing In-Order, Pre-Order, Post-Order Traversal in B-Tree")
            print("99. Exit")
            x = int(input("enter you option? "))
            if x==1: self.print_OrderTraversal()
            if x==99: return

app = btree1()
app.menu()            
