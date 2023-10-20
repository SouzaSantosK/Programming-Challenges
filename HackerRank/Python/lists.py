arr = []
result_array = []

for _ in range(int(input())):
    method, *command = input().split()

    if command != []:
        if len(command) == 2:
            a, b = [int(v) for v in command]
        else:
            a = int(command[0])

    match method:
        case "insert":
            arr.insert(a, b)
        case "print":
            result_array.append(list(arr))
        case "remove":
            arr.remove(a)
        case "append":
            arr.append(a)
        case "sort":
            arr.sort()
        case "pop":
            arr.pop()
        case "reverse":
            arr.reverse()
        case _:
            break

for a in result_array:
    print(a)
