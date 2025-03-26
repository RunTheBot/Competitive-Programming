import sys, heapq
input = sys.stdin.readline
INF = 10**9


class SegTreeCat:
    def __init__(self, A):
        self.n = len(A)
        self.size = 1 << (self.n-1).bit_length()
        self.data = [(INF,0,INF)]*(2*self.size)
        for i in range(self.n):
            self.data[self.size+i] = (A[i], 1, INF)
        for i in range(self.size-1, 0, -1):
            self.data[i] = self._merge(self.data[2*i], self.data[2*i+1])
    
    def _merge(self, left, right):
        m1, c1, s1 = left
        m2, c2, s2 = right
        if m1 < m2:
            m = m1; c = c1; s = min(s1, m2)
        elif m1 > m2:
            m = m2; c = c2; s = min(s2, m1)
        else:
            m = m1; c = c1+c2; s = min(s1, s2)
        return (m, c, s)
    
    def update(self, idx, value):
        
        i = self.size + idx
        self.data[i] = (value, 1, INF)
        while i > 1:
            i //= 2
            self.data[i] = self._merge(self.data[2*i], self.data[2*i+1])
    
    def query_all(self):
        return self.data[1]


class SegTreePen:
    def __init__(self, A):
        self.n = len(A)
        self.size = 1 << (self.n-1).bit_length()
        self.data = [-INF]*(2*self.size)
        for i in range(self.n):
            self.data[self.size+i] = A[i]
        for i in range(self.size-1, 0, -1):
            self.data[i] = max(self.data[2*i], self.data[2*i+1])
    
    def update(self, idx, value):
        i = self.size+idx
        self.data[i] = value
        while i > 1:
            i //= 2
            self.data[i] = max(self.data[2*i], self.data[2*i+1])
    
    def query_all(self):
        return self.data[1]


pens = []  

cat_stats = {}  

cat_to_pens = {}  

cat_index = {}  
cat_list = []  

global_base = 0  

global_heap = []  
global_eligible = []  


def recalc_category(c):
    global global_base
    indices = cat_to_pens.get(c, [])
    best_val = -INF
    second_val = -INF
    cnt = 0
    for i in indices:
        
        if pens[i][1] != c:
            continue
        P = pens[i][0]
        if P > best_val:
            second_val = best_val
            best_val = P
            cnt = 1
        elif P == best_val:
            cnt += 1
        elif P > second_val:
            second_val = P
    old = cat_stats.get(c, (0,0,0))
    
    if c in cat_stats:
        global_base -= cat_stats[c][0]
    cat_stats[c] = (best_val, second_val, cnt)
    global_base += best_val
    
    segTreeCat.update(cat_index[c], best_val)
    
    for i in indices:
        if pens[i][1] != c: continue
        update_pen(i)

def update_pen(i):
    P, c = pens[i]
    best_val, second_val, cnt = cat_stats[c]
    eligible = P if not (P == best_val and cnt == 1) else -INF
    segTreePen.update(i, eligible)
    global_eligible[i] = eligible
    heapq.heappush(global_heap, (-eligible, i))

N, M, Q = map(int, input().split())
for i in range(N):
    C, P = map(int, input().split())
    pens.append([P, C])
    if C not in cat_to_pens:
        cat_to_pens[C] = []
    cat_to_pens[C].append(i)
    global_eligible.append(-INF)

cat_keys = list(cat_to_pens.keys())
cat_keys.sort()  
for idx, c in enumerate(cat_keys):
    cat_index[c] = idx
    best_val = -INF
    second_val = -INF
    cnt = 0
    for i in cat_to_pens[c]:
        P = pens[i][0]
        if P > best_val:
            second_val = best_val
            best_val = P
            cnt = 1
        elif P == best_val:
            cnt += 1
        elif P > second_val:
            second_val = P
    cat_stats[c] = (best_val, second_val, cnt)
    global_base += best_val

A_cat = [cat_stats[c][0] for c in cat_keys]
segTreeCat = SegTreeCat(A_cat)

A_pen = []
for i in range(N):
    P, c = pens[i]
    best_val, second_val, cnt = cat_stats[c]
    eligible = P if not (P == best_val and cnt == 1) else -INF
    A_pen.append(eligible)
    global_eligible[i] = eligible
    heapq.heappush(global_heap, (-eligible, i))
segTreePen = SegTreePen(A_pen)

def calculate_best_score():
    base_score = global_base
    missing = M - len(cat_stats)
    max_improve = 0
    if missing > 0:
        while global_heap and -global_heap[0][0] != global_eligible[global_heap[0][1]]:
            heapq.heappop(global_heap)
        candidate = -global_heap[0][0] if global_heap else -INF
        max_improve = candidate
    else:
        global_min, global_min_count, second_global_min = segTreeCat.query_all()
        for i in range(N):
            P, c = pens[i]
            best_val, second_val, cnt = cat_stats[c]
            target = second_global_min if (best_val == global_min and global_min_count==1) else global_min
            if P <= target:
                continue
            if P == best_val and cnt==1:
                gain = P - target - (best_val - second_val)
            else:
                gain = P - target
            if gain > max_improve:
                max_improve = gain
    return base_score + max_improve

print(calculate_best_score())

for _ in range(Q):
    t, i, x = map(int, input().split())
    i -= 1  
    old_c = pens[i][1]
    if t == 1:
        new_c = x
        pens[i][1] = new_c
        if old_c in cat_to_pens:
            if i in cat_to_pens[old_c]:
                cat_to_pens[old_c].remove(i)
        if old_c in cat_stats:
            if cat_to_pens.get(old_c):
                recalc_category(old_c)
            else:
                global_base -= cat_stats[old_c][0]
                del cat_stats[old_c]
        if new_c not in cat_to_pens:
            cat_to_pens[new_c] = []
        cat_to_pens[new_c].append(i)
        if new_c not in cat_stats:
            cat_stats[new_c] = (-INF, -INF, 0)
            cat_index[new_c] = len(cat_index)
            global_base += 0
        recalc_category(new_c)
        update_pen(i)
    else: 
        pens[i][0] = x
        update_pen(i)
        recalc_category(pens[i][1])
    print(calculate_best_score())








