"""
Peter the painter just finished painting two rectangular paintings and would like to display
both on a rectangular wall which has the smallest perimeter possible. The first painting has
a base of length A units and a height of length B units. The second painting has a base of
length X units and a height of length Y units.
Peter has a few conditions on how to arrange his paintings on the rectangular wall. The first
condition is that the paintings must be upright, meaning that the bases of the paintings are
parallel to the floor. The second condition is that he would like to display both paintings
in full, meaning that they cannot overlap each other. Please help determine the rectangular
wall of minimum perimeter such that the paintings can be displayed without violating his
conditions.
"""

A, B, X, Y = map(int, input().split())

# A is base
# X is base

max_base = max(A, X)
max_height = max(B, Y)

# Add bases
out = 2*(A+X+max_height)

# print(out)

# Add height
out = min(out, 2*(B+Y+max_base))

# print(2*(B+Y+max_base))

print(out)