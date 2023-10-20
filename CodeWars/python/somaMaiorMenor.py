# Some todos os números de um determinado array (cq. list), exceto o elemento mais alto e o mais baixo (por valor, não por índice!).

# O elemento mais alto ou mais baixo, respectivamente, é um único elemento em cada borda, mesmo que haja mais de um com o mesmo valor.

# Exemplo:
# { 6, 2, 1, 8, 10 } => 16
# { 1, 1, 11, 2, 3 } => 6

# Validação de entrada
# Se um valor vazio ( null, None, Nothing, etc. ) for fornecido em vez de um array, ou o array fornecido for uma lista vazia ou uma lista com apenas um elemento, retorne 0.

# Minha resolução:

def sum_array(arr):
    if arr is None or len(arr) <= 1:
        return 0

    arr.remove(max(arr))
    arr.remove(min(arr))
    return sum(arr)


# Inteligente / Boas práticas:

def sum_array2(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0

# --------------------------------------------------------------------------------------------


def sum_array3(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


print(sum_array([6, 2, 1, 8, 10]))
print(sum_array2([6, 2, 1, 8, 10]))
print(sum_array3([6, 2, 1, 8, 10]))
