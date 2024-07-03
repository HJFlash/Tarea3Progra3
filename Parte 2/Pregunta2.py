def floyd_warshall(edges, nodes):
    # Mapeo de nodos a índices
    node_index = {node: idx for idx, node in enumerate(nodes)}
    num_nodes = len(nodes)

    # Inicializar las matrices de distancia, tiempo y costo
    inf = float('inf')
    dist_matrix = [[inf] * num_nodes for _ in range(num_nodes)]
    time_matrix = [[inf] * num_nodes for _ in range(num_nodes)]
    cost_matrix = [[inf] * num_nodes for _ in range(num_nodes)]

    # Configurar las distancias iniciales usando los bordes proporcionados
    for i in range(num_nodes):
        dist_matrix[i][i] = 0
        time_matrix[i][i] = 0
        cost_matrix[i][i] = 0

    for (N_A, N_B, D, T, C) in edges:
        idx_A = node_index[N_A]
        idx_B = node_index[N_B]
        dist_matrix[idx_A][idx_B] = D
        time_matrix[idx_A][idx_B] = T
        cost_matrix[idx_A][idx_B] = C

    # Aplicar el algoritmo de Floyd-Warshall
    for k in range(num_nodes):
        for i in range(num_nodes):
            for j in range(num_nodes):
                if dist_matrix[i][j] > dist_matrix[i][k] + dist_matrix[k][j]:
                    dist_matrix[i][j] = dist_matrix[i][k] + dist_matrix[k][j]
                if time_matrix[i][j] > time_matrix[i][k] + time_matrix[k][j]:
                    time_matrix[i][j] = time_matrix[i][k] + time_matrix[k][j]
                if cost_matrix[i][j] > cost_matrix[i][k] + cost_matrix[k][j]:
                    cost_matrix[i][j] = cost_matrix[i][k] + cost_matrix[k][j]

    return dist_matrix, time_matrix, cost_matrix

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
dist_matrix, time_matrix, cost_matrix = floyd_warshall(edges, nodes)

# Imprimir las matrices resultantes
print("Matriz de distancias:")
for row in dist_matrix:
    print(row)

print("\nMatriz de tiempos:")
for row in time_matrix:
    print(row)

print("\nMatriz de costos:")
for row in cost_matrix:
    print(row)

#ind_E1= nodes.index("E1")
#ind_E5= nodes.index("E5")

#distancia_minima = dist_matrix[ind_E1][ind_E5]
#print(f'La distancia mínima entre E1 y E5 es: {distancia_minima}')

ind_D2 = nodes.index("D2")
ind_D9 = nodes.index("D9")

tiempo_minimo = time_matrix[ind_D2][ind_D9]
print(f'El tiempo mínimo entre D2 y D9 es: {tiempo_minimo}s')