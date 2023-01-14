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
#Define in order traversal
#visit left tree
#visit base node#visit right tree
#define binary search
#value might be in left subtree
#value might be in right subtree

