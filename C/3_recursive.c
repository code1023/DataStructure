#include <stdio.h>

int factorialIterative(int n) {
    int result = 1;

    for (int i = 1; i <= n; i++) result *= i;

    return result;
}

int factorialRecursive(int n) {
    if (n <= 1) return 1;

    return n * factorialRecursive(n - 1);
}

int main(void) {
    printf("반복적으로 구현: %d \n", factorialIterative(5));
    printf("재귀적으로 구현: %d \n", factorialRecursive(5));
    
    return 0;
}
