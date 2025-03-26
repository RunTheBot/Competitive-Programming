def brute_force(S, N, connections):
    graph = [[] for _ in range(N)]
    for s, t, d, u in connections:
        graph[s].append((t, d, u))
        graph[t].append((s, d, u)) 
    
    min_distance = float('inf')
    
    def dfs(current, target, visited, distance, sun_exposure):
        nonlocal min_distance
        
        if current == target:
            if sun_exposure <= S and distance < min_distance:
                min_distance = distance
            return
        
        for neighbor, d, u in graph[current]:
            if not visited[neighbor]:

                sun_add = d if u == 1 else 0
                
                new_distance = distance + d
                new_sun_exposure = sun_exposure + sun_add
                
                if new_sun_exposure <= S:
                    visited[neighbor] = True
                    dfs(neighbor, target, visited, new_distance, new_sun_exposure)
                    visited[neighbor] = False  
        
    visited = [False] * N
    visited[0] = True
    dfs(0, N-1, visited, 0, 0)
    
    return min_distance if min_distance != float('inf') else -1

S = int(input().strip())
N, E = map(int, input().strip().split())

connections = []
for _ in range(E):
    s, t, d, u = map(int, input().strip().split())
    connections.append((s, t, d, u))

# Solve and print output
result = brute_force(S, N, connections)
print(result)
