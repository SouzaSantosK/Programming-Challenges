ballot = int(input())
print(ballot)

register_bank = [0 for i in range(7)]

while ballot != 0:
    if ballot >= 100:
        ballot -= 100
        register_bank[0] += 1
    elif ballot >= 50:
        ballot -= 50
        register_bank[1] += 1
    elif ballot >= 20:
        ballot -= 20
        register_bank[2] += 1
    elif ballot >= 10:
        ballot -= 10
        register_bank[3] += 1
    elif ballot >= 5:
        ballot -= 5
        register_bank[4] += 1
    elif ballot >= 2:
        ballot -= 2
        register_bank[5] += 1
    elif ballot >= 1:
        ballot -= 1
        register_bank[6] += 1

print(f"{register_bank[0]} nota(s) de R$ 100,00")
print(f"{register_bank[1]} nota(s) de R$ 50,00")
print(f"{register_bank[2]} nota(s) de R$ 20,00")
print(f"{register_bank[3]} nota(s) de R$ 10,00")
print(f"{register_bank[4]} nota(s) de R$ 5,00")
print(f"{register_bank[5]} nota(s) de R$ 2,00")
print(f"{register_bank[6]} nota(s) de R$ 1,00")
