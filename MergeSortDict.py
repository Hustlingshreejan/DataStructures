def two_sorted_array(a, b, key, asc):
    sorted = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    if asc:
        while i < len_a and j < len_b:
            if a[i].get(key) <= b[j].get(key):
                sorted.append(a[i])
                i += 1
            else:
                sorted.append(b[j])
                j += 1
        while i < len_a:
            sorted.append(a[i])
            i += 1
        while j < len_b:
            sorted.append(b[j])
            j += 1
        return sorted
    else:
        while i < len_a and j < len_b:
            if a[i].get(key) <= b[j].get(key):
                sorted.append(b[j])
                j += 1
            else:
                sorted.append(a[i])
                i += 1

        while i < len_a:
            sorted.append(a[i])
            i += 1
        while j < len_b:
            sorted.append(b[j])
            j += 1
        return sorted


def merge(arr, key, asc=True):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge(left, key, asc)
    right = merge(right, key, asc)

    return two_sorted_array(left, right, key, asc)


if __name__ == '__main__':
    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]
    aa = [34, 100, 1, 11, 22, 3, 2, 55, 4, 5, 7, 9]
    print(merge(elements, 'age', True))
