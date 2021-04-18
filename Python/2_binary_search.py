def binary_search(arr, target):
    first, last = 0, len(arr) - 1

    while first <= last:
        mid = (first + last) // 2

        if arr[mid] == target:
            return mid
        
        else:
            if target < arr[mid]:
                last = mid - 1
            else:
                first = mid + 1
    
    return -1
    

if __name__ == "__main__":
    arr = [1, 3, 5, 6, 7, 9, 11, 13, 17, 30]
    target = 6
    idx = binary_search(arr, target)

    if idx == -1:
        print('탐색 실패!')
    
    else:
        print(f'타겟 저장 인덱스: {idx}')
