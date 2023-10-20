for _ in range(int(input())):
    main_string = ""
    for char in input():
        if char.isalpha():
            if ord(char) + 3 < 127:
                main_string += chr(ord(char) + 3)
            else:
                char_value = 97 if char.islower() else 65
                main_string += chr((ord(char) - char_value + 3) % 26 + char_value)
        else:
            main_string += char

    main_string = main_string[::-1]

    second_string = main_string[len(main_string) // 2 :]

    third_string = ""

    for char in second_string:
        third_string += chr(ord(char) - 1)

    main_string = main_string[: len(main_string) // 2] + third_string

    print(f"{main_string}")

# Comentar depois

# for _ in range(int(input())):
#     cp_string = ""
#     for char in input():
#         if char.islower() or char.isupper() and char.isalpha():
#             char_value = 97 if char.islower() else 65
#             # cp_string += chr((ord(char) - char_value + 3) % 26 + char_value)
#             if ord(char) + 3 < 127:
#                 cp_string += chr(ord(char) + 3)
#             else:
#                 cp_string += chr((ord(char) - char_value + 3) % 26 + char_value)
#         else:
#             cp_string += char

#     cp_string = cp_string[::-1]

#     sub_string = cp_string[len(cp_string) // 2 :]

#     for char in sub_string:
#         sub_string = sub_string.replace(char, chr(ord(char) - 1))

#     cp_string = cp_string[: len(cp_string) // 2] + sub_string

#     print(f"{cp_string}")