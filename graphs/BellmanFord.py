inf = float("inf")

def BellmanFord(G, s):
    n = len(G)
    dist = [inf] * n
    parents = [None] * n

    dist[s] = 0

    for _ in range(n - 1):
        for u in range(n):
            for v, v_weight in G[u]:
                if dist[u] != inf and dist[u] + v_weight < dist[v]:
                    dist[v] = dist[u] + v_weight
                    parents[v] = u

    for _ in range(n - 1):
        for u in range(n):
            for v, v_weight in G[u]:
                if dist[u] != inf and dist[u] + v_weight < dist[v]:
                    # graph contains a negative cycle !
                    return None, None
    return dist, parents


def find_shortest_path_BF(G, s, e):
    dist, parents = BellmanFord(G, s)

    if dist is None or parents is None:
        return []

    path = []

    if dist[e] == inf:
        return path
    curr = e
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    path.reverse()
    return path
