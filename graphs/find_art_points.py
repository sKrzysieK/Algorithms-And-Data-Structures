# Graph Representation: Adjacency List

def find_art_points(G):
    n = len(G)
    visited = [False] * n
    parents = [None] * n
    distances = [float("inf")] * n
    low = [float("inf")] * n
    is_ap = [False] * n

    time = 0

    def visit(u):
        nonlocal visited
        nonlocal parents
        nonlocal distances
        nonlocal low
        nonlocal time
        nonlocal is_ap

        children = 0

        visited[u] = True
        distances[u] = time
        low[u] = time
        time += 1

        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                children += 1
                visit(v)
                low[u] = min(low[u], low[v])

                if parents[u] is None and children > 1:
                    is_ap[u] = True
                if parents[u] is not None and low[v] >= distances[u]:
                    is_ap[u] = True
            elif v != parents[u]:
                low[u] = min(low[u], distances[v])

    for u in range(n):
        if not visited[u]:
            visit(u)
    return is_ap


def print_art_points(G):
    n = len(G)
    is_ap = find_art_points(G)
    ap = []
    for u in range(n):
        if is_ap[u]:
            ap.append(u)
    print(ap)
