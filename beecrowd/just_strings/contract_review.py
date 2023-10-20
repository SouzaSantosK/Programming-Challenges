while True:
    digit, original_value = map(int, input().split())

    if digit == 0 and original_value == 0:
        break

    original_value = str(original_value)
    original_value = original_value.replace(str(digit), "")
    original_value = original_value.lstrip("0")

    if original_value == "":
        print(0)
    else:
        print(int(original_value))

# Comentar depois

# digit, original_value = input().split()

# new_value = []

# for v in original_value:
#     new_value.append(int(v))

# if digit in new_value:
#     new_value.remove(int(digit))

# counter = sum(new_value)

# if counter == 0:
#     print(counter)
# else:
#     new_value = list(map(str, new_value))
#     print("".join(new_value).lstrip("0"))
