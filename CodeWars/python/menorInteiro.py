# Dada uma matriz de inteiros, sua solução deve encontrar o menor inteiro.

# Por exemplo:
# Dado que [34, 15, 88, 2] sua solução retornará 2
# Dado que [34, -345, -1, 100] sua solução retornará -345
# Você pode assumir, para o propósito deste kata, que o array fornecido não estará vazio.

# Minha solução:

lista = [34, -345, -1, 100]  # Valor de exemplo


def find_smallest_int(arr):
    for i in arr:
        for j in arr:
            if (i > j):
                i = j
    return i

# Inteligente e boas práticas:


def find_smallestInt(arr):
    arr.sort()
    return arr[0]

# --------------------------------------------------------------------------------------------


def findSmallestInt(arr):
    return min(arr)


print(find_smallest_int(lista))
print(find_smallestInt(lista))
print(findSmallestInt(lista))
