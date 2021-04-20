def selection_sort(array):
    for i in range(len(array)):
        min_idx = i     # 가장 작은 원소의 인덱스

        for j in range(i + 1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j
        
        array[i], array[min_idx] = array[min_idx], array[i]

    return array


if __name__ == "__main__":
    array = [7, 5, 9, 0, 3, 1, 2, 4, 6]
    assert(selection_sort(array) == sorted(array))
    print("테스트 통과!")
