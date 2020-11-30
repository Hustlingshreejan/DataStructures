class CompanyTree:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.children = []
        self.parent = None

    def set_position(self, position):
        self.position = position

    def add_child(self, name):
        name.parent = self
        self.children.append(name)

    def get_depth(self):
        depth = 0
        p = self.parent
        while p:
            depth += 1
            p = p.parent
        return depth


    def print_tree(self,user):
        if user == 1:
            value = self.name + " " + f"({self.position})"
        elif user == 2:
            value = self.name
        elif user == 3:
            value = self.position
        else:
            print("Invalid input.")
            return
        spaces = " " * self.get_depth()*4
        dash = spaces + "|__" if self.parent else ""
        print(dash, value)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree(user)


def generate_tree():
    root = CompanyTree("Nilupal", "CEO")
    CTO_position = CompanyTree("Chimay", "CTO")
    CTO_sub = CompanyTree("Vishwa", "Infrastructure Head")
    CTO_sub.add_child(CompanyTree("Dhaval", "CLoud Manager"))
    CTO_sub.add_child(CompanyTree("Abhjit", "App Manager"))
    CTO_sub2 = CompanyTree("Aamir", 'Application Head')

    CTO_position.add_child(CTO_sub)
    CTO_position.add_child(CTO_sub2)

    HR_Head = CompanyTree("Gels", "HR Head")
    HR_Head.add_child(CompanyTree("Peter", "Recruitment Manager"))
    HR_Head.add_child(CompanyTree("Waqas", "Policy Manager"))

    root.add_child(CTO_position)
    root.add_child(HR_Head)

    return root


if __name__ == '__main__':
    g = generate_tree()
    user = int(input("How do you want to print the tree?\nType,1:Both name and position.\n2:Only name.\n3:Only "
                     "Position\n--->"))
    g.print_tree(user)

