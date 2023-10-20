# Rot13:

def rot13(message):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = alphabet.upper()
    encode = ''

    for l in message:
        if l.isalpha():
            main_alphabet = alphabet_upper if l.isupper() else alphabet

            encode_index = main_alphabet.find(l) + 13
            encode_index = encode_index - 26 if encode_index >= 26 else encode_index

            encode += main_alphabet[encode_index]
        else:
            encode += l

    return encode


print(rot13('Test'))

# Solução do chatGPT:

def rot132(string):
    result = ''
    for char in string:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            rotated_ascii = (ord(char) - ascii_offset + 13) % 26 + ascii_offset
            result += chr(rotated_ascii)
        else:
            result += char
    return result


print(rot132('Test'))
