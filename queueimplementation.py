from _collections import deque


class Queue:

    def __init__(self, queue_size):
        self.size = queue_size
        self.container = deque()
        self.queue_front = None
        self.queue_rear = None

    def enqueue(self, element):
        if len(self.container) >= self.size:
            print("Queue overflow")
        else:
            self.container.append(element)

        if self.queue_front is None and self.queue_rear is None:
            self.queue_front = self.queue_rear = element
        if self.queue_rear is not None:
            self.queue_rear = element

    def dequeue(self):
        if len(self.container) == 0:
            print("Queue underflow")
        else:
            self.container.popleft()
            if len(self.container) == 0:
                self.queue_front = self.queue_rear = None
            else:
                self.queue_front = self.container[0]
                self.queue_rear = self.container[-1]

    def display_queue(self):
        print(self.container)

    def head(self):
        print("front", self.queue_front)

    def tail(self):
        print("rear", self.queue_rear)


if __name__ == '__main__':
    a = Queue(5)
    # a.display_queue()
    a.enqueue(1)
    a.enqueue(45)
    a.enqueue(44)
    a.enqueue(45)
    a.display_queue()
    a.head()
    a.tail()
    a.enqueue(55)
    a.head()
    a.tail()
    print("")
    a.dequeue()
    a.head()
    a.tail()
    print("")
    a.dequeue()
    a.head()
    a.tail()
    print("")
    a.dequeue()
    a.head()
    a.tail()
    print("")
    a.dequeue()
    a.head()
    a.tail()
    print("")
    a.dequeue()
    a.head()
    a.tail()
    print("")
    a.dequeue()
    a.head()
    a.tail()
