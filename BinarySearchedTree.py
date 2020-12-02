class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def add_child(self, data):
        if data == self.data:
            # print("Binary Searched tree cannot have a duplicate value. Duplicate one has been removed")
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTree(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTree(data)

    def get_min(self):
        if self.left:
            return self.left.get_min()
        else:
            return "The minimum value for this tree is", self.data

    def get_max(self):
        if self.right:
            a = self.right.get_max()
            return a
        return self.data

    def inorder_travers(self):
        lis = []
        if self.left:
            lis += self.left.inorder_travers()

        lis.append(self.data)

        if self.right:
            lis += self.right.inorder_travers()

        return lis

    def preorder_travers(self):
        emp = []
        emp.append(self.data)
        if self.left:
            # emp.append(self.left)
            emp += self.left.preorder_travers()
        if self.right:
            # emp.append(self.right)
            emp += self.right.preorder_travers()
        return emp


def print_binary_tree(dataset):
    # print(len(dataset))
    root = BinarySearchTree(dataset[0])
    for i in range(1, len(dataset)):
        root.add_child(dataset[i])
    return root


if __name__ == '__main__':
    all_data = [55, 10, 12, 33, 55, 56, 89, 12, 8, 44, 555, 110]
    shree = print_binary_tree(all_data)
    print(shree.inorder_travers())
    print(shree.get_min())
    print(shree.get_max())
    print(shree.preorder_travers())
