class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 != root2:
            if self.rank[root1] > self.rank[root2]:
                self.parent[root2] = root1
            elif self.rank[root1] < self.rank[root2]:
                self.parent[root1] = root2
            else:
                self.parent[root2] = root1
                self.rank[root1] += 1


def kruskal(graph, num_nodes):
    edges = sorted(graph, key=lambda x: x[2])

    uf = UnionFind(num_nodes)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_weight += weight

    return mst, total_weight


graph = [
    (0, 1, 7), (0, 3, 5),
    (1, 2, 8), (1, 3, 9), (1, 4, 7),
    (2, 4, 5),
    (3, 4, 15), (3, 5, 6),
    (4, 5, 8), (4, 6, 9),
    (5, 6, 11)
]

num_nodes = 7
mst, total_weight = kruskal(graph, num_nodes)
print("最小生成樹:", mst)
print("總權重:", total_weight)
