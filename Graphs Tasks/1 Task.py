n = int(input())

boss_p = []

for i in range(n):
    boss_p.append(int(input()))

def know_level(employ):
    if boss_p[employ] == -1:
        return 1
    else:
        return know_level(boss_p[employ] -1) + 1

answer = 0

for employee in range(n):
    level = know_level(employee)

    if level > answer:
        answer = level

print(answer)

