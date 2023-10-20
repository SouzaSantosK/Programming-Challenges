def get_sum(a, b):
    if a == b:
        return a

    lista = []

    if a > b:
        a, b = b, a

    for i in range(a, b + 1):
        lista.append(i)

    return sum(lista)


print(get_sum(-1, 2))

# Outra resolução:


def get_sum2(a, b):
    if a == b:
        return a

    if a > b:
        a, b = b, a

    return sum([i for i in range(a, b + 1)])


print(get_sum2(-1, 2))

# ----------------------------------------------------------------------------------------------


def get_sum3(a, b):
    return sum(range(min(a, b), max(a, b) + 1))


print(get_sum3(-1, 2))
