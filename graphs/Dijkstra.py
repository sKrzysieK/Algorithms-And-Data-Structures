from queue import PriorityQueue

def Dijkstra(G, s):
    n = len(G)
    dist = [float("inf")] * n
    parents = [None] * n

    pq = PriorityQueue()

    dist[s] = 0
    pq.put(0, s)

    while not pq.empty():
        u_weight, u = pq.get()
        for v, v_dist in G[u]:
            if dist[u] + v_dist < dist[v]:
                dist[v] = dist[u] + v_dist
                parents[v] = u
                pq.put((dist[v], v))

    return dist, parents


def find_shortest_path_Dijkstra(G, s, e):
    dist, parents = Dijkstra(G, s)
    path = []

    if dist[e] == float("inf"):
        return path

    curr = e
    while curr is not None:
        path.append(curr)
        curr = parents[curr]
    path.reverse()

    return path