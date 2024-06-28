import heapq

def Dijkstra(Grafo, Origen):
    Tiempos = {Nodo: (float('inf'), []) for Nodo in range(len(Grafo))}
    Tiempos[Origen] = (0, [])
    Cola = [(0, Origen, [])]
    
    while Cola:
        TiempoActual, NodoActual, Camino = heapq.heappop(Cola)
        if TiempoActual > Tiempos[NodoActual][0]:
            continue
        for Vecino, Tiempo in Grafo[NodoActual]:
            NuevaTiempo = TiempoActual + Tiempo
            NuevoCamino = Camino + [NodoActual]
            if NuevaTiempo < Tiempos[Vecino][0]:
                Tiempos[Vecino] = (NuevaTiempo, NuevoCamino)
                heapq.heappush(Cola, (NuevaTiempo, Vecino, NuevoCamino))
    return Tiempos

Grafo = {
    0: [(1, 150), (2, 200), (3, 100)],
    1: [(4, 85)],
    2: [(5, 340), (6, 520)],
    3: [(7, 200)],
    4: [(8, 160)],
    5: [(9, 300)],
    6: [(8, 260)],
    7: [(9, 60)],
    8: [],
    9: []
}

Tiempos = Dijkstra(Grafo, 0)

for Nodo, (Tiempo, Camino) in Tiempos.items():
    if Nodo == 0:
        continue
    print(f"Desde Santiago a Farmacia {Nodo}")
    print(f"- Tiempo minimo: {Tiempo} minutos")
    NodoDestino = Nodo
    print(f"- Camino: {' -> F'.join(map(str, Camino + [NodoDestino]))}")
    print()
