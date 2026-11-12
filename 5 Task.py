n, m = map(int, input().split())

graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())

    a -= 1
    b -= 1

    graph[a].append((b, w))
    graph[b].append((a, w))


INF = 10**18

dist = [INF] * n
parent = [-1] * n
used = [False] * n

dist[0] = 0


for _ in range(n):

    v = -1

    for i in range(n):
        if not used[i]:
            if v == -1 or dist[i] < dist[v]:
                v = i

    if v == -1:
        break

    if dist[v] == INF:
        break

    used[v] = True

    for u, weight in graph[v]:

        new_dist = dist[v] + weight

        if new_dist < dist[u]:
            dist[u] = new_dist
            parent[u] = v


if dist[n - 1] == INF:
    print(-1)
else:
    path = []

    v = n - 1

    while v != -1:
        path.append(v + 1)
        v = parent[v]

    path.reverse()

    print(*path)