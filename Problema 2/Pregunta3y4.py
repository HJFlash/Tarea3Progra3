import heapq

def Dijkstra(Grafo, Origen, Destino):
    Cola = [(0, Origen)]
    Visto = set()
    while Cola:
        (Costo, Nodo) = heapq.heappop(Cola)
        if Nodo in Visto:
            continue
        Visto.add(Nodo)
        if Nodo == Destino:
            return Costo
        for (SgteNodo, Distancia) in Grafo.get(Nodo, []):
            if SgteNodo not in Visto:
                heapq.heappush(Cola, (Costo + Distancia, SgteNodo))
    return float("inf")

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

Distancia = Dijkstra(Grafo, 0, 9)

KmsPorLitro = 10
PrecioLitro = 1432
CombustibleNecesario = Distancia / KmsPorLitro
PrecioCombustible = CombustibleNecesario * PrecioLitro

print()
print("Desde Santiago a F9")
print(f"Distancia total: {Distancia} kilometros")
print(f"Combustible necesario: {CombustibleNecesario} litros")
print(f"Costo total del combustible necesario: {PrecioCombustible} pesos chilenos")
print()
