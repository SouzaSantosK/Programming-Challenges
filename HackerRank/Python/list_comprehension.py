x = int(input())
y = int(input())
z = int(input())
n = int(input())

PERMUTATION = [
    [a, b, c] for a in range(x + 1) for b in range(y + 1) for c in range(z + 1)
]

matrix = [elem for elem in PERMUTATION if sum(elem) != n]
print(matrix)
