class UnionFind:
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

def boruvka(graph):
    n = len(graph)
    uf = UnionFind(n)
    mst = []

    while len(set(uf.find(i) for i in range(n))) > 1:
        min_edge = [None] * n

        for u in range(n):
            for v, weight in graph[u]:
                root_u = uf.find(u)
                root_v = uf.find(v)
                if root_u != root_v:
                    if min_edge[root_u] is None or min_edge[root_u][2] > weight:
                        min_edge[root_u] = (u, v, weight)
                    if min_edge[root_v] is None or min_edge[root_v][2] > weight:
                        min_edge[root_v] = (u, v, weight)

        for edge in min_edge:
            if edge is not None:
                u, v, weight = edge
                if uf.find(u) != uf.find(v):
                    uf.union(u, v)
                    mst.append((u, v, weight))

    return mst

# Ejemplo de uso
graph = {
    0: [(1, 1), (3, 4)],
    1: [(0, 1), (2, 3), (3, 2)],
    2: [(1, 3), (3, 5)],
    3: [(0, 4), (1, 2), (2, 5)]
}

mst = boruvka(graph)
print(mst)
