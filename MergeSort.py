def merge_two_sorted_list(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)

    i = j = 0
    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i += 1
        else:
            sorted_list.append(b[j])
            j += 1

    while i < len_a:
        sorted_list.append(a[i])
        i += 1

    while j < len_b:
        sorted_list.append(b[j])
        j += 1
    return sorted_list


def merge(arr):
    if len(arr) <= 1:
        return arr
    midpoint = len(arr) // 2
    left_side = arr[:midpoint]
    right_side = arr[midpoint:]

    left = merge(left_side)
    right = merge(right_side)

    return merge_two_sorted_list(left, right)


if __name__ == '__main__':
    a = [11,2,111,1,3,56,346,32,1111]
    print(merge(a))
