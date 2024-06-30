
#1. Conexiones Elegidas:
# Pregunta: ¿Cuáles son las conexiones seleccionadas para construir la red de
# gasoductos minimizando el costo total de instalación? Enumera las conexiones y sus costos.

class DisjointSet:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def buscar(self, u):
        if self.padre[u] != u:
            self.padre[u] = self.buscar(self.padre[u])
        return self.padre[u]

    def union(self, u, v):
        raiz_u = self.buscar(u)
        raiz_v = self.buscar(v)
        if raiz_u != raiz_v:
            if self.rango[raiz_u] > self.rango[raiz_v]:
                self.padre[raiz_v] = raiz_u
            elif self.rango[raiz_u] < self.rango[raiz_v]:
                self.padre[raiz_u] = raiz_v
            else:
                self.padre[raiz_v] = raiz_u
                self.rango[raiz_u] += 1

class KruskalMST:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, peso, capacidad):
        self.edges.append((peso, u, v, capacidad))

    def kruskal(self):
        mst = []
        self.edges.sort()
        disjoint_set = DisjointSet(self.V)

        for edge in self.edges:
            peso, u, v, capacidad = edge
            if disjoint_set.buscar(u) != disjoint_set.buscar(v):
                disjoint_set.union(u, v)
                mst.append(edge)
        return mst

pozos_plantas = {0:'P1', 1:'P2', 2:'P3', 3:'G1', 4:'G2', 5:'G3', 6:'G4', 7:'G5', 8:'G6', 9:'G7'}


if __name__ == "__main__":
    vertices = 10  # Número total de nodos (0 a 9)
    kruskal = KruskalMST(vertices)

    edges = [
        (0, 3, 300, 1000),
        (0, 4, 450, 1500),
        (1, 4, 500, 1200),
        (1, 5, 600, 1300),
        (2, 6, 700, 1400),
        (2, 7, 800, 1600),
        
        (3, 6, 400, 1100),
        (4, 7, 450, 1250),
        (5, 8, 600, 1400),
        (6, 9, 650, 1500),
        (7, 9, 700, 1550),
        (8, 9, 750, 1600)
    ]

    for edge in edges:
        u, v, peso, capacidad = edge
        kruskal.add_edge(u, v, peso, capacidad)

    mst = kruskal.kruskal()

    print("Aristas del MST:")
    for edge in mst:
        peso, u, v, capacidad = edge
        print(f"{pozos_plantas[u]} - {pozos_plantas[v]} con un costo de instalación = {peso}, con una capacidad de: {capacidad} m³/día")
