import string


def to_jaden_case(string):
    string = string.split()
    new_string = []

    for word in string:
        new_string.append(word.capitalize())

    return ' '.join(new_string)


print(to_jaden_case("Sample text"))

# Outras soluções:


def to_jaden_case2(string):
    return ' '.join(word.capitalize() for word in string.split())


print(to_jaden_case2("Sample text"))

# --------------------------------------------------------------------------------------------

toJadenCase = string.capwords

# --------------------------------------------------------------------------------------------


def to_jaden_case3(string):
    list = string.split()
    new_list = [i.capitalize() for i in list]
    return ' '.join(new_list)


print(to_jaden_case3("Sample text"))
