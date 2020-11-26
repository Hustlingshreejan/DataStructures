import time
import threading
import queueimplementation


class Foodorder:

    def __init__(self, p_order):
        self.p_order = p_order

    def place_order(self, foodlist):
        self.foodlist = foodlist
        for food in foodlist:
            print(f"Placing an order for {food}")
            self.p_order.enqueue(food)
            time.sleep(0.5)

    def serve_order(self):
        time.sleep(2)
        while True:
            
            print(f"Food {self.p_order.dequeue()} has been served")
            time.sleep(2)


if __name__ == '__main__':
    orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']
    p_order = queueimplementation.QueueQueue(len(orders))
    fo = Foodorder(p_order)

    t1 = threading.Thread(target=fo.place_order, args=(orders,))
    t2 = threading.Thread(target=fo.serve_order)

    t1.start()
    t2.start()


