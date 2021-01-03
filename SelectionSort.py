def selection_sort(data):
    data_size = len(data)
    for i in range(data_size-1):
        min_value_at = i
        for j in range(min_value_at+1, data_size):
            if data[j] < data[min_value_at]:
                min_value_at = j
        if i != min_value_at:
            data[i], data[min_value_at] = data[min_value_at], data[i]
    return data


a = [222,1,23,4,5,11,2,31,34]
print(selection_sort(a))
