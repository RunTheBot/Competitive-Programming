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
            
            if self.tint[node] > 0:
                self.tree[node] = node_right - node_left + 1
            else:
                if node_left != node_right:
                    self.tree[node] = self.tree[2*node] + self.tree[2*node + 1]
                else:
                    self.tree[node] = 0
            return
            
        mid = (node_left + node_right) // 2
        self.update_range(left, right, val, 2*node, node_left, mid)
        self.update_range(left, right, val, 2*node + 1, mid + 1, node_right)
        
        if self.tint[node] > 0:
            self.tree[node] = node_right - node_left + 1
        else:
            self.tree[node] = self.tree[2*node] + self.tree[2*node + 1]

def solve_tinted_glass_window():
    # Read input
    N = int(input())  # Number of glass pieces
    T = int(input())  # Tint factor threshold
    
    # Store events for sweep line algorithm
    events = []
    max_y = 0
    
    # Process each glass piece
    for _ in range(N):
        xl, yt, xr, yb, ti = map(int, input().split())
        
        events.append((xl, ti, yt, yb))  # Start of rectangle with tint
        events.append((xr, -ti, yt, yb))  # End of rectangle with negative tint
        max_y = max(max_y, yb)
    
    # Sort events by x-coordinate
    events.sort()
    
    # Initialize segment tree
    seg_tree = SegmentTree(max_y + 1)
    
    # Calculate total area
    total_area = 0
    prev_x = events[0][0]
    current_tint = 0
    
    for x, tint_change, y1, y2 in events:
        # Calculate area if tint meets threshold
        if x > prev_x and current_tint >= T:
            covered_length = seg_tree.tree[1]
            area = covered_length * (x - prev_x)
            total_area += area
        
        # Update segment tree and current tint
        seg_tree.update_range(y1, y2-1, 1 if tint_change > 0 else -1)
        current_tint += tint_change
        prev_x = x
    
    return total_area

# Run the solution
print(solve_tinted_glass_window())