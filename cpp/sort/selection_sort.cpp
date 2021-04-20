#include <iostream>

int arr[10] = {7, 5, 9, 0, 3, 1, 6, 2, 4, 8};
int len = sizeof(arr) / sizeof(int);

int main(void) {
    for (int i = 0; i < len; i++) {
        int min_idx = i;

        for (int j = i; j < len; j++) {
            if (arr[min_idx] > arr[j]) min_idx = j;
        }

        int temp = arr[i];
        arr[i] = arr[min_idx];
        arr[min_idx] = temp;
    }

    for (int i = 0; i < len; i++) {
        std::cout << arr[i] << ' ';
    }

    std::cout << '\n';

    return 0;
}
