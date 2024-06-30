""" Cantidad de Combustible Necesaria:○
Calcula la cantidad de combustible necesaria para viajar desde Santiago a Copiapó,
asumiendo un consumo de 10 kilómetros por litro."""

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

# el algoritmo de Dijkstra
def dijkstra(grafo, inicio):
    # Distancias desde el nodo de inicio a todos los demás nodos
    distancias = {nodo: float('inf') for nodo in grafo}
    distancias[inicio] = 0
    # MinHeap para seleccionar el nodo con la distancia más pequeña
    min_heap = [(0, inicio)]
    # Guardar los pasos del algoritmo
    pasos = []

    while min_heap:
        distancia_actual, nodo_actual = heapq.heappop(min_heap)
        # Guardar el estado actual
        pasos.append((distancia_actual, nodo_actual, list(min_heap), dict(distancias)))

        # Si la distancia actual es mayor que la distancia registrada, continuamos
        if distancia_actual > distancias[nodo_actual]:
            continue
        
        # Recorremos los nodos vecinos
        for vecino, peso in grafo[nodo_actual]:
            distancia = distancia_actual + peso
            
            # Si se encuentra una distancia más corta
            if distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(min_heap, (distancia, vecino))
                # Guardar el estado después de actualizar la distancia
                pasos.append((distancia, vecino, list(min_heap), dict(distancias)))
    
    return distancias, pasos


distancias_desde_santiago, pasos = dijkstra(grafo, 'Santiago')


i = 0
for paso in pasos:
    distancia, nodo, heap, distancias = paso
    print(f"--- Iteración {i+1} ---")
    print(f"Nodo actual: {nodo}")
    print(f"Distancia actual: {distancia} km")
    print(f"Cola de prioridad (MinHeap): {heap}")
    print(f"Distancias: {distancias}")
    print("-----------------------\n")
    i += 1

# Distancia más corta a Copiapó
distancia_a_copiapo = distancias_desde_santiago.get('Copiapó', 'No hay ruta directa')

# Consumo de combustible (10 km por litro)
if distancia_a_copiapo != 'No hay ruta directa' and distancia_a_copiapo != float('inf'):
    combustible_necesario = distancia_a_copiapo / 10
    print(f"Cantidad de combustible necesaria para viajar desde Santiago a Copiapó: {combustible_necesario:.2f} litros")
else:
    print("No se puede calcular el combustible necesario porque no hay una ruta directa a Copiapó")