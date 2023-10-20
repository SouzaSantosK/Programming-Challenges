# Escreva um programa que encontre a somatoria de todo número de 1 a n. O número sempre será um inteiro positivo maior que 0.

# Por exemplo (Input -> Output):
# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)

# Minha resolução:

def summation(num):
    acm = 0
    for i in range(1, num + 1):
        acm += i
    return acm

print(summation(8))
