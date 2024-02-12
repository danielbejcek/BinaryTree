
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

    """Method that prints values in ascending order."""
    def inOrderTraversal(self):
        if self.left:
            self.left.inOrderTraversal()
        """In case self.left is None (there is no left child of the parent node) we visit (print) the value."""
        print(self.data, end=" ")
        if self.right:
            self.right.inOrderTraversal()

    def preOrderTraversal(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preOrderTraversal()
        if self.right:
            self.right.preOrderTraversal()

    def postOrderTraversal(self):
        if self.left:
            self.left.postOrderTraversal()
        if self.right:
            self.right.postOrderTraversal()
        print(self.data, end=" ")

root = Node(8)
root.insertNode(9)
root.insertNode(4)
root.insertNode(3)
root.insertNode(6)
root.insertNode(2)
root.insertNode(1)
root.insertNode(8)
root.insertNode(10)

root.inOrderTraversal()
print("\n")
root.preOrderTraversal()
print("\n")
root.postOrderTraversal()


