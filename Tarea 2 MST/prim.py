import heapq

def prim(edges):
    graph = {}
    for weight, u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append((v, weight))
        graph[v].append((u, weight))

    start_node = list(graph.keys())[0]
    visited = set([start_node])
    min_heap = []

    for neighbor, weight in graph[start_node]:
        heapq.heappush(min_heap, (weight, start_node, neighbor))

    mst = []

    while min_heap:
        weight, u, v = heapq.heappop(min_heap)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))
            for neighbor, weight in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (weight, v, neighbor))

    return mst

# Lista de las primeras 20 aristas
edges = [
    (10, 65, 644), (3, 68, 355), (35, 39, 91), (59, 11, 808), (48, 26, 140),
    (56, 48, 326), (5, 41, 412), (71, 50, 159), (31, 74, 889), (74, 64, 410),
    (2, 7, 440), (55, 42, 92), (14, 3, 203), (35, 77, 767), (60, 66, 606),
    (26, 35, 696), (71, 23, 783), (12, 22, 372), (22, 71, 155), (65, 42, 18)
]

minimum_spanning_tree = prim(edges)
print("Árbol de expansión mínima:", minimum_spanning_tree)
