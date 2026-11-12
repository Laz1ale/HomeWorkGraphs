n, m = map(int, input().split())

cats = list(map(int, input().split()))

graph = [[] for _ in range(n)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    x -= 1
    y -= 1

    graph[x].append(y)
    graph[y].append(x)

answer = 0


def dfs(point, parent, cats_in_row):
    global answer

    if cats[point] == 1:
        cats_in_row += 1
    else:
        cats_in_row = 0

    if cats_in_row > m:
        return

    is_leaf = True

    for next_point in graph[point]:
        if next_point == parent:
            continue

        is_leaf = False
        dfs(next_point, point, cats_in_row)

    if is_leaf:
        answer += 1


dfs(0, -1, 0)

print(answer)