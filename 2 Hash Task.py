t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    count = {}
    answer = 0

    for i in range(n):
        x = a[i] - i

        answer += count.get(x, 0)

        count[x] = count.get(x, 0) + 1

    print(answer)