#Binary Tree

#Pseudocode

#Define binary tree node class
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    #Add a subtree(child)
    def add_child(self, data):
        if data == self.data:
            return #if node already exist

        #Add data in left subtree
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        
        #Add data in right subtree
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    #define binary search
    def search(self, val):
        if self.data == val:
            return True

        #value might be in left subtree
        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False
                
#value might be in right subtree
#Define in order traversal
#visit left tree
#visit base node#visit right tree

