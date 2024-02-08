import random

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insertNode(self, data):
        if self.data == None:
            self.data = data

        else:

            if data < self.data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insertNode(data)
            if data > self.data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insertNode(data)

    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        print(self.data, end=" ")
        if self.right:
            self.right.inOrderTraversal()

root = Node(8)
root.insertNode(4)
root.insertNode(3)
root.insertNode(6)
root.insertNode(2)
root.inOrderTraversal()

