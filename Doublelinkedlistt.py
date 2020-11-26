class Node:
    def __init__(self,element=None, prev=None, next=None):
        self.element = element
        self.prev = prev
        self.next = next

class DoubleLinedList:
    def __init__(self):
        self.head = None

    def add_beginning(self, element):
        new_node = Node(element, None, self.head)
        self.head = new_node

    def add_end(self, element):
        if self.head is None:
            print("Empty")
        itr1 = self.head
        while itr1.next is not None:
            itr1 = itr1.next
        itr1.next = Node(element, itr1.next, None)

    def show_Doublelinkedlist(self):
        if self.head is None:
            print("Empty")
        iter2 = self.head
        Llstr = ''
        while iter2:
            Llstr += '<---'+str(iter2.element) + '--->'
            iter2 = iter2.next
        print(Llstr)

    def get_len(self):
        count = 0
        itr3 = self.head
        while itr3:
            count += 1
            itr3 = itr3.next
        return count

    
dll= DoubleLinedList()
dll.add_beginning(2)
dll.add_beginning(3)
dll.add_beginning(5)
dll.show_Doublelinkedlist()
dll.add_end(4)
dll.show_Doublelinkedlist()
dll.add_end(4444)
dll.show_Doublelinkedlist()
dll.add_beginning(333)
dll.show_Doublelinkedlist()
print(dll.get_len())



