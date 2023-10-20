# Dada uma matriz não vazia de números inteiros, retorne o resultado da multiplicação dos valores em ordem.
# Exemplo:
# [1, 2, 3, 4] => 1 * 2 * 3 * 4 = 24

# Funciona, mas não é essa a ideia:
import math


def grow(arr):
    return math.prod(arr)

# Agora sim:


def grow1(arr):
    product = 1
    for i in range(len(arr)):
        product *= arr[i]
    return product


print(grow([1, 2, 3, 4]))
print(grow1([1, 2, 3, 4]))
