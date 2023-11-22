from queue import Queue

def topological_sort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parents = [None for _ in range(n)]

    output = []

    def visit(u):
        nonlocal visited
        nonlocal parents

        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                visit(v)
        output.append(u)

    for u in range(n):
        if not visited[u]:
            visit(u)

    return output