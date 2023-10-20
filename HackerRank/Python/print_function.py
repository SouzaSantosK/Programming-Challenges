n = int(input())

number = []

for i in range(n + 1):
    if i != 0:
        number.append(i)

print(number)
for n in number:
    print(n, end="")
