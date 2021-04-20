from collections import defaultdict


def count_sort(array):
    result, cnt_list = [], defaultdict(list)

    for x in array:
        cnt_list[x].append(x)

    for x in range(min(cnt_list), max(cnt_list) + 1):
        result.extend(cnt_list[x])
    
    return result


array = [7, 5, 9, 0, 3, 1, 6, 1, 9, 10, 30, 3, 8, 20, 0, 5, 2]
print(count_sort(array)) 
