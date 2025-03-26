class SegmentTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (4 * size)
        self.tint = [0] * (4 * size)
        
    def update_range(self, left, right, val, node=1, node_left=0, node_right=None):
        if node_right is None:
            node_right = self.size - 1
            
        if right < node_left or left > node_right:
            return
            
        if left <= node_left and node_right <= right:
            self.tint[node] += val
            return
            
        mid = (node_left + node_right) // 2
        self.update_range(left, right, val, 2*node, node_left, mid)
        self.update_range(left, right, val, 2*node + 1, mid + 1, node_right)
        
    def query_range(self, threshold, node=1, node_left=0, node_right=None):
        if node_right is None:
            node_right = self.size - 1
            
        if self.tint[node] >= threshold:
            return node_right - node_left + 1
            
        if node_left == node_right:
            return 0
            
        mid = (node_left + node_right) // 2
        total_tint = self.tint[node]
        
        left_sum = self.query_range(threshold - total_tint, 2*node, node_left, mid)
        right_sum = self.query_range(threshold - total_tint, 2*node + 1, mid + 1, node_right)
        
        return left_sum + right_sum


N = int(input())
T = int(input())

events = []
coords_y = set()

for _ in range(N):
    x1, y1, x2, y2, t = map(int, input().split())
    events.append((x1, 1, y1, y2, t))
    events.append((x2, -1, y1, y2, t))
    coords_y.add(y1)
    coords_y.add(y2)

coords_y = sorted(list(coords_y))
y_map = {y: i for i, y in enumerate(coords_y)}

events.sort()

seg_tree = SegmentTree(len(coords_y))

total_area = 0
prev_x = events[0][0]

for x, event_type, y1, y2, tint in events:
    if x > prev_x:
        covered_length = seg_tree.query_range(T)
        if covered_length > 0:
            real_length = 0
            for i in range(len(coords_y) - 1):
                if seg_tree.query_range(T, 1, i, i) > 0:
                    real_length += coords_y[i + 1] - coords_y[i]
            total_area += real_length * (x - prev_x)
    
    seg_tree.update_range(y_map[y1], y_map[y2]-1, event_type * tint)
    prev_x = x

print(total_area)
