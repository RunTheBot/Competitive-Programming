#include <iostream>
#include <string>

int main() {
    long long min = 1;
    long long max = 2 * (long long)(1e9);

    while (true) {
        long long guess = (min + max) >> 1;
        std::cout << guess << std::endl;

        std::string result;
        std::cin >> result;

        if (result == "FLOATS") {
            max = guess - 1;
        } else if (result == "SINKS") {
            min = guess + 1;
        } else {
            break;
        }
    }

    return 0;
}
