array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:]

    left_list = [x for x in tail if x <= pivot]
    right_list = [x for x in tail if x > pivot]

    # 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행하고, 전체 리스트 반환
    return quick_sort(left_list) + [pivot] + quick_sort(right_list)

print(quick_sort(array))
