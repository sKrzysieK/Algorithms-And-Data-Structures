# Graph Representation: Adjacency List

def find_bridges(G):
    n = len(G)
    visited = [False] * n
    parents = [None] * n
    distances = [float("inf")] * n
    low = [float("inf")] * n

    time = 0

    output = []

    def visit(u):
        nonlocal visited
        nonlocal parents
        nonlocal distances
        nonlocal low
        nonlocal time

        visited[u] = True
        distances[u] = time
        low[u] = time

        time += 1

        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                visit(v)
                low[u] = min(low[u], low[v])

                if low[v] > distances[u]:
                    output.append((u, v))
            elif v != parents[u]:
                low[u] = min(low[u], distances[v])

    for u in range(n):
        if not visited[u]:
            visit(u)
    return output
