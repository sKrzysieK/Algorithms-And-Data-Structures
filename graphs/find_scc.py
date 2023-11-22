# Graph Representation: Adjacency List

def find_SCC(G):
    n = len(G)
    visited = [False] * n
    times = [-1] * n
    time = 0

    output = []

    def visit(G, u, cmp):
        nonlocal visited
        nonlocal time
        nonlocal times

        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                cmp = visit(G, v, cmp)
        time += 1
        times[u] = time
        cmp.append(u)
        return cmp

    # run DFS and calc times
    for u in range(n):
        if not visited[u]:
            visit(G, u, [])

    # reverse edges' direction
    newG = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            newG[v].append(u)

    # run DFS in descending times order on new graph
    visited = [False] * n
    while max(times) > -1:
        u = times.index(max(times))
        times[u] = -2
        if not visited[u]:
            cmp = visit(newG, u, [])
            output.append(cmp)

    return output