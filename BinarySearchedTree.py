class BinarySearchedTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            print("Number already exists. Binary Searched tree can only have unique element.")
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchedTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchedTree(data)

    def inorder_traversal(self):
        elements = []
        if self.left:
            elements += self.left.inorder_traversal()

        elements.append(self.data)

        if self.right:
            elements += self.right.inorder_traversal()
        # elements.append(self.data)
        return elements

    def search_element(self, element):
        if element == self.data:
            return True
        if element < self.data:
            if self.left:
                return self.left.search_element(element)
            else:
                return False
        else:
            if self.right:
                return self.right.search_element(element)
            else:
                return False
def BinaryTree(lis):
    root = BinarySearchedTree(lis[0])
    for i in range(1, len(lis)):
        root.add_child(lis[i])
    return root



if __name__ == '__main__':
    data = [100,70,101,50,80,81,75,25,60,30,10]
    a = BinaryTree(data)
    print(a.inorder_traversal())
    print(a.search_element(666))
