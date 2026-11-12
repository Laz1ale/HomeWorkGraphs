names = set()

n=int(input())

for i in range(n):
    name = input()
    if name not in names:
        names.add(name)
        print('ОК')
    else:
        i = 1

        while name + str(1) in names:
            i += 1

        edit_name = name + str(i)

        names.add(edit_name)
        print(names)

