def dfs(graph, start, visited):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            stack.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

def is_connected(graph, n):
    visited = set()
    dfs(graph, 0, visited)
    return len(visited) == n

def reverse_delete(graph):
    edges = [(u, v, weight) for u in graph for v, weight in graph[u]]
    edges = sorted(edges, key=lambda x: x[2], reverse=True)
    
    for u, v, weight in edges:
        # Eliminar arista
        graph[u].remove((v, weight))
        graph[v].remove((u, weight))
        
        # Verificar si el grafo sigue siendo conexo
        if not is_connected(graph, len(graph)):
            # Si no es conexo, volver a agregar la arista
            graph[u].append((v, weight))
            graph[v].append((u, weight))
    
    # Construir el MST resultante
    mst = []
    for u in graph:
        for v, weight in graph[u]:
            if (v, u, weight) not in mst:
                mst.append((u, v, weight))
    
    return mst

# Ejemplo de uso
graph = {
    0: [(1, 1), (3, 4)],
    1: [(0, 1), (2, 3), (3, 2)],
    2: [(1, 3), (3, 5)],
    3: [(0, 4), (1, 2), (2, 5)]
}

mst = reverse_delete(graph)
print(mst)
