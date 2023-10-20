records = []

records = []

for _ in range(int(input())):
    name = input()
    score = float(input())

    records.append([name, score])

# Ordenando a lista com base nas notas
records.sort(key=lambda x: x[1])

# Listando somente as notas e removendo as duplicadas, ordenando de forma crescente, pegando a 2° menor
lowest_score = sorted(list(set(score for name, score in records)))[1]

# Listando o nome dos estudantes que tem a mesma 2° menor nota
lowest_students = [name for name, score in records if score == lowest_score]

for name in sorted(lowest_students):
    print(name)
