n = int(input())
a = [[0]*n for i in range(n)]

for i in range(n):
    for k in range(n):
        if i == n - k -1:
            a[i][k] = 1
        elif i > n - k - 1:
            a[i][k] = 2


for line in a:
    for el in line:
        print(el, end = ' ')
    print()


