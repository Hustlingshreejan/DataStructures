def merge_two_sorted_list(a,b, arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1

    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1


def merge(arr):
    if len(arr) <= 1:
        return
    midpoint = len(arr) // 2
    left_side = arr[:midpoint]
    right_side = arr[midpoint:]

    merge(left_side)
    merge(right_side)

    merge_two_sorted_list(left_side, right_side,arr)


if __name__ == '__main__':
    a = [11,2,111,1,3,56,346,32,1111]
    merge(a)
    print(a)
