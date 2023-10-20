# Você obtém uma matriz de números, retorna a soma de todos os positivos.

# Minha resolução:
def positive_sum(arr):
    acm = 0
    for i in range(len(arr)):
        if (arr[i] > 0):
            acm += arr[i]
    return acm


# Inteligentes / Boas práticas:


def positiveSum(arr):
    return sum(x for x in arr if x > 0)


print(positive_sum([1, -4, 7, 12]))
print(positiveSum([1, -4, 7, 12]))
