import sys
import collections

input = sys.stdin.readline

R, S = map(int, input().split())
trees = [0]*R
for r in range(R):
    row = input().strip()
    for c, ch in enumerate(row):
        if ch == 'x':
            trees[r] |= (1 << c)

G = int(input())
res = []
for _ in range(G):
    r, s = map(lambda x: int(x) - 1, input().split())
    # BFS to find nearest tree
    visited = [0]*R
    q = collections.deque([(r, s, 0)])
    visited[r] |= (1 << s)
    best = None
    while q:
        rr, cc, dist = q.popleft()
        if (trees[rr] & (1 << cc)) != 0:
            best = dist**2
            break
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = rr+dr, cc+dc
            if 0 <= nr < R and 0 <= nc < S:
                if (visited[nr] & (1 << nc)) == 0:
                    visited[nr] |= (1 << nc)
                    q.append((nr, nc, dist+1))
    res.append(str(best))
    trees[r] |= (1 << s)  # add new tree
print("\n".join(res))