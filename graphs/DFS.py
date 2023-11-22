# Time Complexity: O()
# Graph Representation: Adjacency List

def DFS(G):
    n = len(G)
    visited = [False] * n
    parents = [None] * n

    def visit(u):
        nonlocal visited
        nonlocal parents

        visited[u] = True

        for v in G[u]:
            if not visited[v]:
                parents[v] = u
                visit(v)

    for u in range(n):
        if not visited[u]:
            visit(u)

    return visited, parents
