value = float(input())

print("NOTAS:")
notas = [100, 50, 20, 10, 5, 2]
for nota in notas:
    qtd_notas = int(value // nota)
    print(f"{qtd_notas} nota(s) de R$ {nota:.2f}")
    value %= nota

print("MOEDAS:")
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
for moeda in moedas:
    qtd_moedas = int(value // moeda)
    print(f"{qtd_moedas} moeda(s) de R$ {moeda:.2f}")
    value = round(value % moeda, 2)
