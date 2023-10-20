# kata: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list2(l):
    filtered_list = []

    for element in l:
        if type(element) == int:
            filtered_list.append(element)
    return filtered_list

# Outra resolução:

def filter_list(l):
    # filtered_list = [element for element in l if type(element) == int]
    # return filtered_list

    # return [element for element in l if isinstance(element, int)]
    return [element for element in l if type(element) is int]


print(filter_list([1, 'a', 'b', 0, 15]))
