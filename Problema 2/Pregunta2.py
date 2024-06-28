import heapq

def Dijkstra(Grafo, Origen, Destino):
    Distancias = {Nodo: float('inf') for Nodo in Grafo}
    Distancias[Origen] = 0
    ColaPrioridad = [(0, Origen)]
    Tiempos = {Nodo: float('inf') for Nodo in Grafo}
    Tiempos[Origen] = 0

    while ColaPrioridad:
        DistanciaActual, NodoActual = heapq.heappop(ColaPrioridad)

        if DistanciaActual > Distancias[NodoActual]:
            continue

        for Vecino, Peso, Tiempo in Grafo[NodoActual]:
            Distancia = DistanciaActual + Peso
            TiempoTotal = Tiempos[NodoActual] + Tiempo

            if Distancia < Distancias[Vecino]:
                Distancias[Vecino] = Distancia
                Tiempos[Vecino] = TiempoTotal
                heapq.heappush(ColaPrioridad, (Distancia, Vecino))

    return Distancias[Destino], Tiempos[Destino]

Grafo = {
    0: [(1, 50, 150), (2, 100, 200), (3, 150, 100)],
    1: [(4, 100, 85)],
    2: [(5, 150, 340), (6, 200, 520)],
    3: [(7, 250, 200)],
    4: [(8, 200, 160)],
    5: [(9, 300, 300)],
    6: [(8, 250, 260)],
    7: [(9, 100, 60)],
    8: [],
    9: []
}

NodoOrigen = 0
NodoDestino = 9
DisMasCorta, TiempoEstimado = Dijkstra(Grafo, NodoOrigen, NodoDestino)

print()
print("Santiago a F9:")
print(f"- La distancia mas corta es de {DisMasCorta} kilometros")
print(f"- El tiempo estimado de viaje es de {TiempoEstimado} minutos")
print()
