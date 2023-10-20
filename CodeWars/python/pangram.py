# Pangram: https://www.codewars.com/kata/545cedaa9943f7fe7b000048/train/python

def is_pangram(s):
    alphabet = []
    for char in s:
        if char.isalpha():
            alphabet.append(char.lower())

    alphabet = list(set(alphabet))
    return True if len(alphabet) == 26 else False

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))


# Outra resolução:


def is_pangram2(s):
    # alphabet = list(set([char.lower() for char in s if char.isalpha()]))
    # return True if len(alphabet) == 26 else False
    return True if len(list(set([char.lower() for char in s if char.isalpha()]))) == 26 else False


print(is_pangram2("gazeta publica hoje: breve anuncio de faxina na quermesse"))

# --------------------------------------------------------------------------------------------


def is_pangram3(s):
    print(s)
    s = s.lower()
    for char in 'abcdefghijklmnopqrstuvwxyz':
        if char not in s:
            return False
    return True


print(is_pangram3("The quick, brown fox jumps over the lazy dog!"))
