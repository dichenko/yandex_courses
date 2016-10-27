n = int(input())
li = []



d = {}
for i in range(n):
    x = int(input())
    if x in d.keys():
        li.append(d[x])
    else:
        d[x] = f(x)
        li.append(d[x])

for el in li:
    print(el)
