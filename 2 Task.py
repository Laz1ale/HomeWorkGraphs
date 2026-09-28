n = int(input())

f = list(map(int, input().split()))

for i in range(n):
    first = f[i] - 1
    second = f[first] - 1
    third = f[second] - 1

    if third == i and i != first and i != second and first != second:
        print("YES")
        break
else:
    print("NO")