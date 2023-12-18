# DWITE '09 R6 #5 - Air Travel Planning
# DMOJ: https://dmoj.ca/problem/dwite09c6p5

import heapq

def dijkstra(graph, start, end):
    # Initialize distances and paths.
    distances = {node: float('inf') for node in graph}

    # print(distances)
    distances[start] = 0
    # previous_nodes = {}

    # Priority queue to keep track of the nodes to visit next.
    queue = [(0, start)]

    while queue:
        currentDistance, currentNode = heapq.heappop(queue)

        if currentNode == end:
            return currentDistance

        # Explore the neighbors of the current node.
        for neighbor, weight in graph[currentNode].items():
            distance = currentDistance + weight

            # If shorter path to the Next Node, update its shortedst distance and path.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # previous_nodes[neighbor] = currentNode
                heapq.heappush(queue, (distance, neighbor))


def main():
    graph = {}

    n = int(input())
    for i in range(n):
        # Node Start, Node End, Distance
        start, end, distance = input().split()

        distance = int(distance)

        if start in graph:
            graph[start][end] = distance
        else:
            graph[start] = {end: distance}

        graph["SEA"] = {}

    print(dijkstra(graph, "YYZ", "SEA"))




main()
main()
main()
main()
main()

