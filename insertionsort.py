
class InsertionSort:
    def insertionsort(self, elements):
        for i in range(1, len(elements)):
            anchor = elements[i]
            j = i - 1
            print(elements)
            while j >= 0 and anchor < elements[j]:
                elements[j+1] = elements[j]
                j = j - 1
            elements[j + 1] = anchor
            print(anchor)
        return elements


e = [38, 51, 1, 5, 77]
a = InsertionSort()
print(a.insertionsort(e))
