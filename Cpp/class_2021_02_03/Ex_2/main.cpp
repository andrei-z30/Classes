#include <iostream>

int main() {
    std::cout << "Sum numbers:" << std::endl;
    int n, result = 0;
    std::cin >> n;
    for (int i = 1; i <= n; i++) {
        result += i;
    }
    std::cout << "Result: " << result;
    return 0;
}
