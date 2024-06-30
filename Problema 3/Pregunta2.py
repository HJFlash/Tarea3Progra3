""" Distancia a una Ciudad Específica:
○ ¿Cuál es la distancia más corta estimada de viaje desde Santiago a Copiapó?  """



import heapq

# Grafo de las ciudades y distancias
grafo = {
    'Santiago': [('Valparaíso', 115), ('Concepción', 500), ('La Serena', 471), ('Copiapó', 806)],
    'Valparaíso': [('Antofagasta', 1376)],
    'Concepción': [('Temuco', 221), ('Punta Arenas', 2000)],
    'La Serena': [('Antofagasta', 1000), ('Iquique', 1450)],
    'Antofagasta': [('Iquique', 510)],
    'Temuco': [('Puerto Montt', 300)],
    'Punta Arenas': [('Puerto Montt', 2000)],
    'Copiapó': [('La Serena', 390), ('Antofagasta', 841), ('Iquique', 1150)],
    'Iquique': [],
    'Puerto Montt': []
}

# Función para el algoritmo de Dijkstra
def dijkstra(grafo, inicio):
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    min_heap = [(0, inicio)]
    pasos = []

    while min_heap:
        distancia_actual, nodo_actual = heapq.heappop(min_heap)
        pasos.append((distancia_actual, nodo_actual, list(min_heap), dict(distancias)))

        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in grafo[nodo_actual]:
            distancia = distancia_actual + peso

            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(min_heap, (distancia, vecino))
                pasos.append((distancia, vecino, list(min_heap), dict(distancias)))

    return distancias, pasos

# Ejecutar Dijkstra desde Santiago
distancias_desde_santiago, pasos = dijkstra(grafo, 'Santiago')

# Imprime los pasos detallados
for i, paso in enumerate(pasos):
    distancia, nodo, heap, distancias = paso
    print(f"--- Iteración {i+1} ---")
    print(f"Nodo actual: {nodo}")
    print(f"Distancia actual: {distancia} km")
    print(f"Cola de prioridad (MinHeap): {heap}")
    print(f"Distancias: {distancias}")
    print("-----------------------\n")

# Distancia más corta a Copiapó
distancia_a_copiapo = distancias_desde_santiago.get('Copiapó', 'No hay ruta directa')
print(f"Distancia más corta desde Santiago a Copiapó: {distancia_a_copiapo} km")