inf = float("inf")

def FloydWarshall(G):
    n = len(G)
    dist = [ [ inf for _ in range(n) ] for _ in range(n) ]
    next = [ [ None for _ in range(n) ] for _ in range(n) ]

    # converting adjacency list to adjacency matrix
    AM = [[inf for _ in range(n)] for _ in range(n)]
    for u in range(n):
        for v, vWeight in G[u]:
            AM[u][v] = vWeight

    # dist and next setup
    for i in range(n):
        for j in range(n):
            dist[i][j] = AM[i][j]
            if AM[i][j] != inf:
                next[i][j] = j

    # execute algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next[i][j] = next[i][k]

    # detect and propagate negative cycles
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = -inf
                    next[i][j] = None

    return dist, next


def find_shortest_path_FW(G, s, e):
    path = []
    dist, next = FloydWarshall(G)

    # checking if path exists
    if dist[s][e] == inf:
        return path

    curr = s
    while curr != e:
        if curr is None:
            return None
        path.append(curr)
        curr = next[curr][e]

    if next[curr][e] is None:
        return None
    path.append(e)

    return path