# Алгоритм
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)

    print(start)

    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


graph = {'0': set(['4', '2']),
         '1': set(['1', '3']),
         '2': set(['2', '4'])}

dfs(graph, '0')