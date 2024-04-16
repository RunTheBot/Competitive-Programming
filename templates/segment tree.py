class SegmentTree:
    def __init__(self, nums, operation=min, neutral=float('inf')):
        self.n = len(nums)
        self.operation = operation
        self.neutral = neutral
        self.tree = [self.neutral] * (4 * self.n)
        self.build(nums, 1, 0, self.n - 1)

    def build(self, nums, tree_idx, left, right):
        if left == right:
            self.tree[tree_idx] = nums[left]
        else:
            mid = (left + right) // 2
            self.build(nums, 2 * tree_idx, left, mid)
            self.build(nums, 2 * tree_idx + 1, mid + 1, right)
            self.tree[tree_idx] = self.operation(
                self.tree[2 * tree_idx], self.tree[2 * tree_idx + 1])

    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, tree_idx, left, right, idx, val):
        if left == right:
            self.tree[tree_idx] = val
        else:
            mid = (left + right) // 2
            if idx <= mid:
                self._update(2 * tree_idx, left, mid, idx, val)
            else:
                self._update(2 * tree_idx + 1, mid + 1, right, idx, val)
            self.tree[tree_idx] = self.operation(
                self.tree[2 * tree_idx], self.tree[2 * tree_idx + 1])

    def query(self, q_left, q_right):
        return self._query(1, 0, self.n - 1, q_left, q_right)

    def _query(self, tree_idx, left, right, q_left, q_right):
        if q_left > right or q_right < left:
            return self.neutral
        if q_left <= left and q_right >= right:
            return self.tree[tree_idx]
        mid = (left + right) // 2
        left_val = self._query(2 * tree_idx, left, mid, q_left, q_right)
        right_val = self._query(2 * tree_idx + 1, mid + 1, right, q_left, q_right)
        return self.operation(left_val, right_val)

# Example usage:

# Define custom operations (e.g., min, max, sum)
def custom_min(a, b):
    return min(a, b)

def custom_max(a, b):
    return max(a, b)

def custom_sum(a, b):
    return a + b

# Create Segment Tree instances with different operations
nums = [1, 3, 2, -1, 4, 5]
min_segment_tree = SegmentTree(nums, operation=custom_min)
max_segment_tree = SegmentTree(nums, operation=custom_max, neutral=float('-inf'))
sum_segment_tree = SegmentTree(nums, operation=custom_sum, neutral=0)

# Example queries
print(min_segment_tree.query(0, 3))  # Output: -1 (minimum in range [0, 3])
print(max_segment_tree.query(1, 4))  # Output: 4 (maximum in range [1, 4])
print(sum_segment_tree.query(2, 5))  # Output: 10 (sum in range [2, 5])

# Update an element
min_segment_tree.update(2, -3)
print(min_segment_tree.query(0, 3))  # Output: -3 (minimum in range [0, 3] after update)
