# Time Complexity: O(|V| + |E|)
# |V| - number of graph's vertices
# |E| - number of graph's edges
# Graph Representation: Adjacency List

from queue import Queue


def BFS(G, s):
    n = len(G)
    q = Queue()

    visited = [False] * n
    distance = [-1] * n
    parents = [None] * n

    visited[s] = True
    distance[s] = 0
    q.put(s)

    while not q.empty():
        u = q.get()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                distance[v] = distance[u] + 1
                parents[v] = u
                q.put(v)

    return visited, distance, parents