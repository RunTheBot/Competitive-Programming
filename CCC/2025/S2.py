import sys

input = sys.stdin.readline

RLE = input().strip()
segments = []

curr_letter = None
curr_number = ""

for ch in RLE:
    if ch.isalpha():
        if curr_letter is not None:
            segments.append((curr_letter, int(curr_number)))
        curr_letter = ch
        curr_number = ""
    else:
        curr_number += ch
segments.append((curr_letter, int(curr_number))) 

n = int(input().strip())
total_length = sum(count for _, count in segments)
mod_index = n % total_length

for letter, count in segments:
    if mod_index < count:
        print(letter)
        break
    mod_index -= count
