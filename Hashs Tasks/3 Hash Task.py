t = int(input())

MOD1 = 1_000_000_007
MOD2 = 1_000_000_009
BASE = 911382323

for _ in range(t):
    n = int(input())
    s = input()

    power1 = [1] * (n + 1)
    power2 = [1] * (n + 1)

    for i in range(1, n + 1):
        power1[i] = (power1[i - 1] * BASE) % MOD1
        power2[i] = (power2[i - 1] * BASE) % MOD2

    prefix1 = [0] * (n + 1)
    prefix2 = [0] * (n + 1)

    for i in range(n):
        value = ord(s[i]) - ord('a') + 1

        prefix1[i + 1] = (
            prefix1[i] * BASE + value
        ) % MOD1

        prefix2[i + 1] = (
            prefix2[i] * BASE + value
        ) % MOD2

    hashes = set()

    for i in range(n - 1):

        left1 = prefix1[i]
        left2 = prefix2[i]

        right_len = n - i - 2

        right1 = (
            prefix1[n]
            - prefix1[i + 2] * power1[right_len]
        ) % MOD1

        right2 = (
            prefix2[n]
            - prefix2[i + 2] * power2[right_len]
        ) % MOD2

        result1 = (
            left1 * power1[right_len] + right1
        ) % MOD1

        result2 = (
            left2 * power2[right_len] + right2
        ) % MOD2

        hashes.add((result1, result2))

    print(len(hashes))
