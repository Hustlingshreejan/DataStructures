class GeneralTree:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_depth(self):
        depth = 0
        p = self.parent
        while p:
            depth += 1
            p = p.parent
        return depth

    def print_tree(self):
        spaces = "  " * self.get_depth() * 2
        prefix = spaces + "|__" if self.parent else ""
        print(prefix, self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()




def build_product_tree():
    root = GeneralTree('Electronics')

    laptop = GeneralTree('Laptop')
    laptop.add_child(GeneralTree('dell'))
    laptop.add_child(GeneralTree('lenovo'))
    laptop.add_child(GeneralTree('MSI'))

    phone = GeneralTree('Phone')
    Iphone = GeneralTree("Iphone")
    Iphone.add_child(GeneralTree('IphoneX'))
    Iphone.add_child(GeneralTree('IphoneXI'))
    phone.add_child(Iphone)
    phone.add_child(GeneralTree('Samsung'))
    phone.add_child(GeneralTree('MI'))

    root.add_child(laptop)
    root.add_child(phone)

    return root


if __name__ == "__main__":
    tree_from_root = build_product_tree()
    tree_from_root.print_tree()
