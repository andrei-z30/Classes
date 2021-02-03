#include <iostream>

int main() {
    std::cout << "Input number 5 char:" << std::endl;
    char num[5];
    std::cin >> num;
    for (int i = 0; i < 5; i++) {
        std::cout << num[i] << std::endl;
    }
    return 0;
}
