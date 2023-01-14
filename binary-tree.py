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
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    #Define in order traversal
    def in_order_traversal(self):
        elements = []
        if self.left: #visit left tree
            elements += self.left.in_order_traversal()

        elements.append(self.data)

        if self.right: #visit right tree
            elements += self.right.in_order_traversal()
                
        return elements 

def build_tree(elements):
    print("Building tree with these elements: ", elements)
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__=='__main__':
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    country_tree = build_tree(countries)

    print("UK is in the list? ", country_tree.search("UK"))
    print("Sweden is in the list? ", country_tree.search("Sweden"))
    print(country_tree.in_order_traversal())

    numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
    print("In order traversal gives this sorted list:",numbers_tree.in_order_traversal())

#Source:
#https_://www.youtube.com/watch?v=lFq5mYUWEBk