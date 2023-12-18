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
