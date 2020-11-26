from queue import Queue

class QueueQueue:
    """
    collections deque has been used to store a data. If you want to make thread friendly, it will be best
    to use from queue import Queue instead of deque.
    """

    def __init__(self, queue_size):
        self.size = queue_size
        self.container = Queue(maxsize=len(self.size))
        self.queue_front = None
        self.queue_rear = None

    def enqueue(self, element):
        if len(self.container) >= self.size:
            print("Queue overflow")
        else:
            self.container.put(element)

        if self.queue_front is None and self.queue_rear is None:
            self.queue_front = self.queue_rear = element
        if self.queue_rear is not None:
            self.queue_rear = element

    def dequeue(self):
        if len(self.container) == 0:
            print("Queue underflow")
        else:
            self.container.get()
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

    def queue_len(self):
        if len(self.container) == 0:
            print("Size is 0. Its empty")
        else:
            print(len(self.container))


if __name__ == '__main__':
    a = QueueQueue(5)
    a.queue_len()
