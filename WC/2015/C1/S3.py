"""
Woburn Challenge 2015-16 Round 1 - Senior Division

It's no surprise that the Programming Enrichment Group at Woburn participates in a wide number of programming contests. However, not all contests are held at the same place (worry not – the Woburn Challenge finals will be held at a single location). In fact if too many people register for a contest, the contest organizers may even demand that the same contest be held in two entirely different towns! This will make it a lot harder for our young Woburnites to compete in the contest, but certainly won't stop them from trying.

There are \(N\) \((2 \le N \le 10^5)\) towns uniquely numbered with integers from \(1\) to \(N\), and \(M\) \((1 \le M \le 10^5)\) one-way roads running amongst them. Specifically, the \(i\)-th road (for \(i = 1 \dots M\)) allows one to travel from a town \(A_i\) to a different town \(B_i\) \((1 \le A_i, B_i \le N; A \ne B)\) and has a distance of \(D_i\) \((1 \le D_i \le 100)\) kilometres. No two roads run between the same pair of towns in the same direction. A very large programming contest is soon to be held across two locations, with the main contest site located in town \(1\) and the secondary contest site located in town \(2\). A non-zero number of Woburnites will be competing in this contest, with \(C_i\) \((0 \le C_i \le 10^6)\) of them living in town \(i\) (for each \(i = 1 \dots N\)). Each competitor must select one of the two contest sites and travel to it using a sequence of roads. This sequence is possibly empty, if they're fortunate enough to live in the same town as their chosen contest site.

There is a catch! Resources are limited at the second contest site, so the contest organizers have insisted that no more than \(K\) \((0 \le K \le 10^9)\) of the competitors attend the secondary site (located in town \(2\)). Given that the Woburnites collaborate to come up with the best travel strategy, you must help them determine the minimum total combined distance that they must travel in order to all attend the contest, such that no more than \(K\) of them travel to the secondary site.

In test cases worth 60% of the marks, \(N \le 100\).
In a subset of those cases worth 30% of the marks, \(C_i \le 1\) (for \(i = 1 \dots N\)).

Input Specification
Line \(1\) of input will contain three space-separated integers, the values of \(N\), \(M\), and \(K\), respectively representing the number of towns, roads, and the maximum number of Woburnites that may attend the second site.
There will be \(N\) lines to follow. The \(i\)-th of these lines (for \(i = 1 \dots N\)) will contain a single integer \(C_i\), representing the number of Woburnites living in town \(i\).
There will be \(M\) lines to follow. The \(i\)-th of these lines (for \(i = 1 \dots M\)) will contain three space-separated integers, the values of \(A_i\), \(B_i\), and \(D_i\) representing the \(i\)-th one-way road.

Output Specification
The output should consist of a single integer. If it is possible for the Woburnites to travel to all contest sites with no more than \(K\) of them attending the secondary site, then output the minimum total combined distance that they must travel to do so. Output -1 if it is impossible for all of them to reach a contest site while satisfying the condition. Please note that the answer may not necessarily fit in a 32-bit integer.

"""

# import networkx as nx
# import matplotlib.pyplot as plt

# def visualize_graph(graph):
#     # Create a directed graph
#     G = nx.DiGraph()
    
#     # Add edges with weights
#     for node in range(1, len(graph)):
#         for neighbor, weight in graph[node].items():
#             G.add_edge(node, neighbor, weight=weight)
    
#     # Create the layout
#     pos = nx.spring_layout(G)
    
#     # Draw the graph
#     plt.figure(figsize=(10, 8))
    
#     # Draw nodes
#     nx.draw_networkx_nodes(G, pos, node_color='lightblue', 
#                           node_size=500)
    
#     # Draw edges
#     nx.draw_networkx_edges(G, pos, edge_color='gray',
#                           arrows=True, arrowsize=20)
    
#     # Add node labels
#     nx.draw_networkx_labels(G, pos)
    
#     # Add edge labels
#     edge_labels = nx.get_edge_attributes(G, 'weight')
#     nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
#     plt.title("Graph Visualization")
#     plt.axis('off')
#     plt.show()


import sys
import heapq

# Fast input reading
input = sys.stdin.readline

# Read N (towns), M (roads), and K (max competitors at site 2)
N, M, K = map(int, input().split())

# Read number of Woburnites in each town (1-based indexing)
C = [0]  # Add a dummy value at index 0
for i in range(N):
    C.append(int(input()))

# Create adjacency lists for the graph
graph = [[] for _ in range(N + 1)]  # 1-based indexing
for _ in range(M):
    a, b, d = map(int, input().split())
    # Store reversed edges with distances
    graph[b].append((a, d))

# print("graph:", graph)
# visualize_graph(graph)

def get_shortest_distances(graph, start):
    distances = [float('inf')] * len(graph)
    distances[start] = 0
    queue = [(0, start)]
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue
            
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
                
    return distances

dist_site1 = get_shortest_distances(graph, 1)
dist_site2 = get_shortest_distances(graph, 2)

total_distance = 0
remaining_k = K
towns_to_sort = []  

for town in range(1, N + 1):
    if C[town] == 0: 
        continue
        
    D1 = dist_site1[town]
    D2 = dist_site2[town]
    
    if D1 == float('inf') and D2 == float('inf'):
        print(-1)
        sys.exit()
        
    elif D1 == float('inf'):
        if remaining_k >= C[town]:
            total_distance += C[town] * D2
            remaining_k -= C[town]
        else:
            print(-1) 
            sys.exit()
            
    elif D1 <= D2:
        total_distance += C[town] * D1
        
    else:
        towns_to_sort.append((D1 - D2, town))

towns_to_sort.sort(reverse=True)

for diff, town in towns_to_sort:
    D1 = dist_site1[town]
    D2 = dist_site2[town]
    count = C[town]
    to_site2 = min(remaining_k, count)
    to_site1 = count - to_site2
    
    total_distance += to_site2 * D2  
    total_distance += to_site1 * D1  
    remaining_k -= to_site2

print(total_distance)





