from _collections import deque

class Stack:
    def __init__(self, stack_size):
        self.size = stack_size
        self.container = deque()

    def push(self, element):
        if len(self.container) >= self.size:
            return "'Stack overflow', Stack is full"
        else:
            self.container.append(element)

    def pop(self):
        if len(self.container) == 0:
            return "'Stack underflow', Stack has no element to pop"
        else:
            self.container.pop()

    def top(self):
        return "Top ->", self.container[-1]

    def is_empty(self):
        return len(self.container) == 0


    def is_full(self):
        return len(self.container) == self.size

    def display_stack(self):
        return self.container


if __name__ == '__main__':


    a = Stack(5)
    a.push(5)
    a.push(4)
    a.push(3)
    a.push(2)
    # a.push(1)
    print(a.display_stack())
    print(a.top())
    a.pop()
    print(a.display_stack())
    print(a.top())
    a.push(22)
    print(a.display_stack())
    print(a.top())



