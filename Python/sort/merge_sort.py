def merge_sort(array):
    if len(array) < 2:
        return array

    mid = len(array) // 2
    low_array = merge_sort(array[:mid])
    high_array = merge_sort(array[mid:])

    result = []
    low, high = 0, 0
    
    while low < len(low_array) and high < len(high_array):
        if low_array[low] < high_array[high]:
            result.append(low_array[low])
            low += 1
        else:
            result.append(high_array[high])
            high += 1
    
    result += low_array[low:]
    result += high_array[high:]
    
    return result
