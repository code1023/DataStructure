#include <stdio.h>

int BinarySearch(int arr[], int first, int last, int target) {
    int mid;
    
    if (first > last)
        return -1;      // 탐색 실패
    
    mid = (first + last) / 2;   // 탐색 대상의 중간 인덱스
    if (arr[mid] == target)
        return mid;             // 탐색된 타겟의 인덱스 값 반환
    
    else if (target < arr[mid])
        return BinarySearch(arr, first, mid - 1, target);
    
    else
        return BinarySearch(arr, mid + 1, last, target);
}

int main() {
    int arr[] = {1, 3, 5, 9, 10, 7};
    int idx;
    
    idx = BinarySearch(arr, 0, sizeof(arr)/sizeof(int)-1, 9);
    if (idx == -1)
        printf("탐색 실패! \n");
    else
        printf("타겟 저장 인덱스: %d \n", idx);
    
    return 0;
}
