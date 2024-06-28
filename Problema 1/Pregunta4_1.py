# 4 Impacto de Restricciones de Capacidad:
# ○ Pregunta: Si se introduce una nueva restricción que requiere que la capacidad total
# mínima en cualquier camino entre dos pozos de gas debe ser al menos 1200 m³/día,
# ¿cómo afecta esto al diseño de la red?
# ○ Pregunta: Si se introduce una nueva restricción que requiere que la capacidad total
# mínima en cualquier camino entre dos pozos de gas debe ser al menos 1300 m³/día,
# ¿cómo afecta esto al diseño de la red?


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

class KruskalMST:
    def __init__(self, vertices):
        self.V = vertices
        self.edges = []

    def add_edge(self, u, v, weight, capacity):
        self.edges.append((weight, u, v, capacity))

    def kruskal(self):
        mst = []
        self.edges.sort()
        disjoint_set = DisjointSet(self.V)

        for edge in self.edges:
            weight, u, v, capacity = edge
            if capacity >= 1200:  # Verificar que la capacidad sea al menos 1200 m³/día
                if disjoint_set.find(u) != disjoint_set.find(v):
                    disjoint_set.union(u, v)
                    mst.append(edge)

        return mst

# Ejemplo de uso
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
        u, v, weight, capacity = edge
        kruskal.add_edge(u, v, weight, capacity)

    mst = kruskal.kruskal()
    costo_total = 0
    print("Aristas del MST:")
    for edge in mst:
        weight, u, v, capacity = edge
        print(f"{u} - {v} con peso {weight} y capacidad {capacity}")
        
