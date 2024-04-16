def topological_sort(graph):
    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        result.append(node)

    visited = set()
    result = []

    for node in graph:
        if node not in visited:
            dfs(node)

    return result[::-1]
