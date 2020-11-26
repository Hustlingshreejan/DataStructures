class Node:
    def __init__(self, element=None, node=None):
        self.element = element
        self.node = node


class Linkedlist:
    def __init__(self):
        self.head = None

    def add_beginning(self, element):
        new_element = Node(element, None)
        new_element.next = self.head
        self.head = new_element

    def add_end(self, element):
        new_element = Node(element, None)
        if self.head is None:
            new_element = self.head
            new_element.next = None

        iterr = self.head
        while iterr.next is not None:
            iterr = iterr.next
        iterr.next = new_element
        new_element.next = None

    def get_length(self):
        count = 0
        itr3 = self.head
        while itr3:
            count += 1
            itr3 = itr3.next
        return count

    def remove_element(self, index):
        if self.head is None:
            print("Empty")

        if index < 0 | index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr4 = self.head
        while itr4:
            if count == index-1:
                itr4.next = itr4.next.next
            itr4 = itr4.next
            count += 1

    def add_from_index(self, index, element):
        if index < 0 | index > self.get_length():
            raise Exception("Invalid Index")
        if index == 0:
            self.add_beginning(element)

        count = 0
        itr5 = self.head
        while itr5:
            if count == index-1:
                new_element = Node(element, itr5.next)
                new_element.next = itr5.next
                itr5.next = new_element

            itr5 = itr5.next
            count += 1

    def show_linkedlist(self):
        if self.head is None:
            print("Empty")
        iter2 = self.head
        Llstr = ''
        while iter2:
            Llstr += str(iter2.element) + '--->'
            iter2 = iter2.next
        print(Llstr)

    def insert_after_value(self, searched_value, new_value):
        itr6 = self.head
        while itr6:
            if itr6.element == searched_value:
                print(f'The new value {new_value} will be added after the element {searched_value}')
                new_element = Node(new_value, itr6.next)
                new_element.next = itr6.next
                itr6.next = new_element
                return
            itr6 = itr6.next
        else:
            print("Value not found")

if __name__ == '__main__':
    print("Name of all methods:\n1:add_beginning.\n2:add_end.\n3:get_length.\n4:remove_element.\n5:add_from_index.\n6:show_linkedlist.\n7insert_after_value."
          "\n###########################")
    ll = Linkedlist()
    ll.add_beginning(1)
    ll.add_end(22)
    ll.show_linkedlist()
    ll.add_from_index(1, 55)
    ll.show_linkedlist()
    ll.insert_after_value(22, 44)
    ll.show_linkedlist()
