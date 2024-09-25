# Amplitude Hackathon Summer '24 Problem 4 - Spenser's Big Announcement
# DMOJ: https://dmoj.ca/problem/ampl2024sp4

def can_fit(width, n, l, s, word_widths):
    lines = 1
    current_line_width = 0
    words_in_line = 0

    for w in word_widths:
        if words_in_line > 0:
            if current_line_width + s + w <= width:
                current_line_width += s + w
                words_in_line += 1
            else:
                lines += 1
                if lines > l:
                    return False
                current_line_width = w
                words_in_line = 1
        else:
            current_line_width = w
            words_in_line = 1

    return True


n, l, s = map(int, input().split())
word_widths = list(map(int, input().split()))

left = max(word_widths)
right = sum(word_widths) + (n - 1) * s
while left < right:
    mid = (left + right) // 2
    if can_fit(mid, n, l, s, word_widths):
        right = mid
    else:
        left = mid + 1


print(left)