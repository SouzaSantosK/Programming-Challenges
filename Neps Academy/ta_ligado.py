n, m = [int(v) for v in input().split()]

grafo = [[] for _ in range(n + 1)]

for i in range(m):
    t, a, b = [int(v) for v in input().split()]
    if t == 0:
        if a in grafo[b]:
            print(1)
        else:
            print(0)
    else:
        grafo[a].append(b)
        grafo[b].append(a)
