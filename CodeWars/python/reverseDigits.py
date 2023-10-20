# Convert numbers into reverse numbers matrix: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

def digitize2(n):
    list_number = []
    for number in str(n):
        list_number.append(int(number))

    return list_number[::-1]


# Outra versão:
def digitize(n):
    # list_number = [int(number) for number in str(n)]
    # return list_number[::-1]

    return [int(number) for number in str(n)][::-1]


print(digitize(35231))


def digitize3(n):
    return list(map(int, reversed(str(n))))

print(digitize3(35231))
