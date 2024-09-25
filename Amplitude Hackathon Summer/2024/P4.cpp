#include <iostream>
#include <vector>
#include <algorithm>

bool can_fit(int width, int n, int l, int s, const std::vector<int>& word_widths) {
    int lines = 1;
    int current_line_width = 0;
    int words_in_line = 0;

    for (int w : word_widths) {
        if (words_in_line > 0) {
            if (current_line_width + s + w <= width) {
                current_line_width += s + w;
                words_in_line++;
            } else {
                lines++;
                if (lines > l) {
                    return false;
                }
                current_line_width = w;
                words_in_line = 1;
            }
        } else {
            current_line_width = w;
            words_in_line = 1;
        }
    }

    return true;
}

int main() {
    int n, l, s;
    std::cin >> n >> l >> s;
    std::vector<int> word_widths(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> word_widths[i];
    }

    int left = *std::max_element(word_widths.begin(), word_widths.end());
    int right = std::accumulate(word_widths.begin(), word_widths.end(), 0) + (n - 1) * s;
    
    while (left < right) {
        int mid = left + (right - left) / 2;
        if (can_fit(mid, n, l, s, word_widths)) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    std::cout << left << std::endl;

    return 0;
}
