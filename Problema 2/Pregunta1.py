import heapq

def Dijkstra(Grafo, Origen):
    Distancias = {Nodo: (float('inf'), []) for Nodo in range(len(Grafo))}
    Distancias[Origen] = (0, [])
    Cola = [(0, Origen, [])]
    
    while Cola:
        DistanciaActual, NodoActual, Camino = heapq.heappop(Cola)
        if DistanciaActual > Distancias[NodoActual][0]:
            continue
        for Vecino, Distancia in Grafo[NodoActual]:
            NuevaDistancia = DistanciaActual + Distancia
            NuevoCamino = Camino + [NodoActual]
            if NuevaDistancia < Distancias[Vecino][0]:
                Distancias[Vecino] = (NuevaDistancia, NuevoCamino)
                heapq.heappush(Cola, (NuevaDistancia, Vecino, NuevoCamino))
    return Distancias

Grafo = {
    0: [(1, 50), (2, 100), (3, 150)],
    1: [(4, 100)],
    2: [(5, 150), (6, 200)],
    3: [(7, 250)],
    4: [(8, 200)],
    5: [(9, 300)],
    6: [(8, 250)],
    7: [(9, 100)],
    8: [],
    9: []
}

Distancias = Dijkstra(Grafo, 0)

for Nodo, (Distancia, Camino) in Distancias.items():
    if Nodo == 0:
        continue
    print(f"Desde Santiago a Farmacia {Nodo}")
    print(f"- Distancia minima: {Distancia} kilometros")
    NodoDestino = Nodo
    print(f"- Camino: {' -> F'.join(map(str, Camino + [NodoDestino]))}")
    print()
