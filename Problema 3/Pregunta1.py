"""  1. Rutas Más Cortas:
○ ¿Cuál es la ruta más corta (en Kilometros) desde Santiago a cada una de las
siguientes ciudades: Valparaíso, Concepción, La Serena, Antofagasta, Temuco, Punta
Arenas, Iquique, Puerto Montt, y Copiapó?"""



import heapq


grafo = {
    'Santiago': {'Valparaíso': 115, 'Concepción': 500, 'La Serena': 471},
    'Valparaíso': {'Antofagasta': 1376},
    'Concepción': {'Temuco': 221, 'Punta Arenas': 2000},
    'La Serena': {'Antofagasta': 1000, 'Iquique': 1450},
    'Antofagasta': {'Iquique': 510},
    'Temuco': {'Puerto Montt': 300},
    'Punta Arenas': {'Puerto Montt': 2000},
    'Iquique': {},
    'Puerto Montt': {},
    'Copiapó': {'La Serena': 390, 'Antofagasta': 841, 'Iquique': 1150}
}

# Algoritmo Dijkstra 
def dijkstra(grafo, inicio):
    distancias = {inicio: 0}
    visitados = set()
    fila_prioridad = [(0, inicio)]
    pasos = []

    while fila_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(fila_prioridad)
        pasos.append((distancia_actual, nodo_actual, list(fila_prioridad), dict(distancias), set(visitados)))

        if nodo_actual in visitados:
            continue

        visitados.add(nodo_actual)
        
        for vecino, peso in grafo[nodo_actual].items():
            distancia_total = distancia_actual + peso

            if vecino not in distancias or distancia_total < distancias[vecino]:
                distancias[vecino] = distancia_total
                heapq.heappush(fila_prioridad, (distancia_total, vecino))
                pasos.append((distancia_total, vecino, list(fila_prioridad), dict(distancias), set(visitados)))

    return distancias, pasos

# Se calcula las distancias mínimas desde Santiago a cada ciudad del grafo
distancias_mínimas, pasos = dijkstra(grafo, 'Santiago')

# Se Imprime los pasos detallados
for i, paso in enumerate(pasos):
    distancia, nodo, heap, distancias, visitados = paso
    print(f"--- Iteración {i+1} ---")
    print(f"Nodo actual: {nodo}")
    print(f"Distancia actual: {distancia} km")
    print(f"Cola de prioridad (MinHeap): {heap}")
    print(f"Distancias: {distancias}")
    print(f"Visitados: {visitados}")
    print("-----------------------\n")

# Se imprime las distancias mínimas
print("Distancias mínimas desde Santiago:")
for ciudad, distancia in distancias_mínimas.items():
    print(f"{ciudad}: {distancia} km")