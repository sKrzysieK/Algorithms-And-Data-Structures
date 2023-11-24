class Node:
    def __init__(self, value):
        self.parent = self
        self.rank = 0
        self.value = value


class Kruskal:
    def __init__(self, G):
        self.G = G
        self.n = len(G)
        self.edges = self.make_edges()
        self.nodes = self.make_nodes()

        self.edges.sort(key=lambda item: item[2])

        self.mst = []
        self.minCost = 0

    def make_nodes(self):
        nodes = []
        for u in range(self.n):
            nodes.append(Node(u))
        return nodes

    def make_edges(self):
        edges = []
        for u in range(self.n):
            for v, w in self.G[u]:
                edges.append((u, v, w))
        return edges

    def find(self, x):
        if x.parent != x:
            x.parent = self.find(x.parent)
        return x.parent

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x.rank > y.rank:
            y.parent = x
        else:
            x.parent = y
            if x.rank == y.rank:
                y.rank += 1

    def find_mst(self):
        curr_mst_edge = 0
        i = 0

        while curr_mst_edge < self.n - 1:
            u, v, w = self.edges[i]
            i += 1

            x = self.find(self.nodes[u])
            y = self.find(self.nodes[v])

            if x != y:
                curr_mst_edge += 1
                self.mst.append((u,v,w))
                self.minCost += w
                self.union(x, y)

        return self.mst, self.minCost

    def print_result(self):
        for u, v, w in self.mst:
            print("( ", u, ", ", v, " ), w: ", w, ", ")
        print("Minimum Cost: ", self.minCost)
