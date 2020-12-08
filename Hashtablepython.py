class HashTable:
    def __init__(self):
        self.max = 100
        self.arr = [[] for x in range(self.max)]

    def hashval(self, key):
        h = 0
        for character in key:
            h += ord(character)
        return h % self.max

    def __setitem__(self, key, value):
        d = self.hashval(key)
        found = False
        for ind, element in enumerate(self.arr[d]):
            if len(element) == 2 and element[0] == key:
                self.arr[d][ind] = (key, value)
                found = True
                break
        if not found:
            self.arr[d].append((key, value))

    def __getitem__(self, item):
        b = self.hashval(item)
        for element in self.arr[b]:
            if element[0] == item:
                return element[1]

    def __delitem__(self, key):
        a = self.hashval(key)
        for ind, element in enumerate(self.arr[a]):
            if element[0] == key and len(element) == 2:
                del self.arr[a][ind]

if __name__ == '__main__':

    aa = HashTable()
    aa.__setitem__("march 6", 22)
    aa.__setitem__("march 17", 455)

    print(aa.arr)
    print(aa.__getitem__("march 6"))
