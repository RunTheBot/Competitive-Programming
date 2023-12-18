// 2020 Canadian Computing Competition
// Senior division
// Problem S3: Searching for Strings
// DMOJ: https://dmoj.ca/problem/ccc20s3
#include <iostream>
#include <vector>

std::vector<std::string> permute(const std::string& str) {
    std::vector<std::string> permutations;
    if (str.length() == 1) {
        return {str};
    } else {
        for (size_t i = 0; i < str.length(); ++i) {
            if (str[i] != str.find(str[i])) {
                continue;
            }
            for (const auto& permutation : permute(str.substr(0, i) + str.substr(i + 1))) {
                permutations.push_back(str[i] + permutation);
            }
        }
        return permutations;
    }
}

int main() {
    std::string match, str;
    std::cin >> match >> str;

    int count = 0;

    for (const auto& permutation : permute(match)) {
        if (str.find(permutation) != std::string::npos) {
            ++count;
        }
    }

    std::cout << count << std::endl;

    return 0;
}
