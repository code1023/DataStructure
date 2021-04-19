#include <iostream>

// 반복적으로 구현한 n!
int factorialIterative(int n) {
    int result = 1;

    for (int i = 1; i <= n; i++) {
        result *= i;
    }

    return result;
}

// 재귀적으로 구현한 n!
int factorialRecursive(int n) {
    if (n <= 1) return 1;

    return n * factorialRecursive(n - 1);
}

int main() {
    // std::cout << "Hello World!\n";
    std::cout << "반복적으로 구현: " << factorialIterative(5) << "\n";
    std::cout << "재귀적으로 구현: " << factorialRecursive(5) << "\n";

    return 0;
}
