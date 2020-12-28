class BubbleSort:

    def __init__(self, array_data):
        self.data = array_data

    def sort_num(self):
        length = len(self.data)
        for i in range(length-1):
            swapped = False
            for j in range(length-1-i):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    swapped = True
            if not swapped:
                break
        print(self.data)

    def sort_dictionary(self, keyname):
        length = len(keyname)
        for i in range(length-1):
            swapped = False
            for j in range(length-1-i):
                if self.data[j].get(keyname) > self.data[j+1].get(keyname):
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]
                    swapped = True
            if not swapped:
                break
        print(self.data)

data = [11,1,111,3,44,2,34,56]
d = [
    {'name':'shreejan', 'Age':22,},
    {'name':'radhey', 'Age':23,},
    {'name':'shreeja', 'Age':24,},
    {'name':'shreejana', 'Age':2,},
    {'name':'ahreejana', 'Age':2,},
]
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
a = BubbleSort(elements)
# a.sort_num()
a.sort_dictionary('name')
