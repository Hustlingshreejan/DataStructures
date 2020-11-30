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
    root_data = input("Set the root:")
    root = GeneralTree(root_data)
    print("The root is in level 0. Set the children for level 1")
    level_one_children = int(input("How  many children of root you want to add? ->"))
    for i in range(level_one_children):
        children_data = input("Set the children name for level 1.")
        instance_name = GeneralTree(children_data)
        user = input(f"Do you have children for {children_data} class? Y or N").upper()
        if user == "Y":
            level_two_children = int(input(f"How many children you want to add inside {children_data}?\n:"))
            for j in range(level_two_children):
                # print(f"Set the children for {children_data}")
                sub_children_data = input(f"Set the children for {children_data}.")
                instance_name.add_child(GeneralTree(sub_children_data))
            root.add_child(instance_name)
        else:
            root.add_child(instance_name)
    # laptop = GeneralTree('Laptop')
    # laptop.add_child(GeneralTree('dell'))
    # laptop.add_child(GeneralTree('lenovo'))
    # laptop.add_child(GeneralTree('MSI'))
    #
    # phone = GeneralTree('Phone')
    # Iphone = GeneralTree("Iphone")
    # Iphone.add_child(GeneralTree('IphoneX'))
    # Iphone.add_child(GeneralTree('IphoneXI'))
    # phone.add_child(Iphone)
    # phone.add_child(GeneralTree('Samsung'))
    # phone.add_child(GeneralTree('MI'))
    #
    # root.add_child(instance_name)
    # root.add_child(phone)

    return root


if __name__ == "__main__":
    tree_from_root = build_product_tree()
    tree_from_root.print_tree()
