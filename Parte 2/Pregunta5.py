def floyd_warshall_with_path(edges, nodes):
    # Mapeo de nodos a índices
    node_index = {node: idx for idx, node in enumerate(nodes)}
    num_nodes = len(nodes)

    # Inicializar las matrices de distancia y predecesores
    inf = float('inf')
    dist_matrix = [[inf] * num_nodes for _ in range(num_nodes)]
    predecessor = [[None] * num_nodes for _ in range(num_nodes)]

    # Configurar las distancias iniciales usando los bordes proporcionados
    for i in range(num_nodes):
        dist_matrix[i][i] = 0

    for (N_A, N_B, D, T, C) in edges:
        idx_A = node_index[N_A]
        idx_B = node_index[N_B]
        dist_matrix[idx_A][idx_B] = D
        predecessor[idx_A][idx_B] = idx_A

    # Aplicar el algoritmo de Floyd-Warshall
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                    predecessor[i][j] = predecessor[k][j]

    return dist_matrix, predecessor

def reconstruct_path(predecessor, start_idx, end_idx):
    path = []
    if predecessor[start_idx][end_idx] is None:
        return path
    current = end_idx
    while current != start_idx:
        path.append(current)
        current = predecessor[start_idx][current]
        if current is None:
            return []  # No hay camino
    path.append(start_idx)
    path.reverse()
    return path

# Nodos y aristas
nodes = ["E1", "E2", "E3", "E4", "E5", "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "D11"]
edges = [
    ("E1", "E2", 10, 1, 1000), ("E1", "E3", 15, 2, 1500), ("E2", "E4", 12, 1.5, 1200), ("E3", "E4", 10, 1, 1000),
    ("E2", "D1", 20, 2, 2000), ("E4", "D2", 5, 0.5, 500), ("D1", "D2", 10, 1, 1000), ("D1", "D3", 25, 2.5, 2500),
    ("D2", "D4", 8, 0.8, 800), ("D3", "D4", 12, 1.2, 1200), ("D3", "D5", 15, 1.5, 1500), ("D4", "D6", 10, 1, 1000),
    ("D5", "D6", 5, 0.5, 500), ("D5", "D7", 7, 0.7, 700), ("D6", "D8", 10, 1, 1000), ("D7", "D8", 12, 1.2, 1200),
    ("D7", "D9", 15, 1.5, 1500), ("D8", "D9", 5, 0.5, 500), ("D9", "D10", 8, 0.8, 800), ("D9", "D11", 10, 1, 1000),
    ("D10", "D11", 12, 1.2, 1200), ("E1", "E4", 25, 3, 3000), ("E2", "D2", 18, 2, 1800), ("E3", "D3", 20, 2, 2000),
    ("E4", "D4", 15, 1.5, 1500), ("D1", "D5", 30, 3, 3000), ("D2", "D6", 25, 2.5, 2500), ("D3", "D7", 28, 2.8, 2800),
    ("D4", "D8", 20, 2, 2000), ("D5", "D9", 22, 2.2, 2200), ("D6", "D10", 18, 1.8, 1800), ("D7", "D11", 30, 3, 3000),
    ("D8", "E5", 25, 2.5, 2500)
]

# Ejecutar el algoritmo
dist_matrix, predecessor = floyd_warshall_with_path(edges, nodes)

ind_D1 = nodes.index("D1")
ind_E5 = nodes.index("E5")
shortest_path_indices = reconstruct_path(predecessor, ind_D1, ind_E5)
shortest_path_nodes = [nodes[idx] for idx in shortest_path_indices]

# Obtener la distancia mínima
min_dist_D1_E5 = dist_matrix[ind_D1][ind_E5]

# Imprimir la distancia mínima y la ruta más corta
print(f"El tiempo mínimo desde E4 hasta D7 es: {min_tiempo_D1_E5} segundos")
print(f"La ruta más corta desde E4 hasta D7 es: {' -> '.join(shortest_path_nodes)}")
