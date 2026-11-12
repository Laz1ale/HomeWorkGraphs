t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())

        u -= 1
        v -= 1

        graph[u].append(v)
        graph[v].append(u)

    color = [-1] * n

    queue = [0]
    color[0] = 0

    main = 0

    while main < len(queue):
        v = queue[main]
        main += 1

        for u in graph[v]:
            if color[u] == -1:
                color[u] = 1 - color[v]
                queue.append(u)

    group0 = []
    group1 = []

    for i in range(n):
        if color[i] == 0:
            group0.append(i + 1)
        else:
            group1.append(i + 1)

    if len(group0) <= len(group1):
        answer = group0
    else:
        answer = group1

    print(len(answer))
    print(*answer)