# Sua tarefa é criar duas funções ( maxe min, ou maximume minimum, etc., dependendo do idioma ) que recebem uma lista de inteiros como entrada e retornam o maior e o menor número dessa lista, respectivamente.

# * [4, 6, 2, 1, 9, 63, -134, 566]      -> max = 566, min = -134
# * [-52, 56, 30, 29, -54, 0, -110]     -> min = -110, max = 56
# * [42, 54, 65, 87, 0]                 -> min = 0, max = 87
# * [5]                                 -> min = 5, max = 5

# Notas:
# Você pode considerar que não haverá arrays/vetores vazios.

def minimum(arr):
    return min(arr)


def maximum(arr):
    return max(arr)


print(maximum([42, 54, 65, 87, 0]))
print(minimum([42, 54, 65, 87, 0]))

# Outras resoluções:


def minimum2(arr):
    min_value = arr[0]
    for i in arr[1:]:
        if i < min_value:
            min_value = i
    return min_value


def maximum2(arr):
    max_value = arr[0]
    for i in arr[1:]:
        if i > max_value:
            max_value = i
    return max_value


print(maximum2([42, 54, 65, 87, 0]))
print(minimum2([42, 54, 65, 87, 0]))

# --------------------------------------------------------------------------------------------


def minimum3(arr):
    arr.sort()
    return arr[0]


def maximum3(arr):
    arr.sort()
    return arr[-1]


print(maximum3([42, 54, 65, 87, 0]))
print(minimum3([42, 54, 65, 87, 0]))
