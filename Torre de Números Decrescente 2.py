rows = 9
for i in range(rows, 0, -1):
    for j in range(rows - i + 1, 0, -1):
        print(j, end=" ")
    print()
input()
