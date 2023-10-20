# Complete a função para que ela encontre a média das três notas passadas a ela e retorne o valor da letra associada a essa nota.

#   Pontuação Numérica	    Letra Nota
# 90 <= pontuação <= 100	    'A'
# 80 <= pontuação < 90	        'B'
# 70 <= pontuação < 80	        'C'
# 60 <= pontuação < 70	        'D'
# 0 <= pontuação < 60	        'F'

# Os valores testados estão todos entre 0 e 100. Não há necessidade de verificar valores negativos ou valores maiores que 100.

def get_grade(s1, s2, s3):
    avg = sum([s1, s2, s3]) / 3
    if 90 <= avg:
        grade = 'A'
    elif 80 <= avg:
        grade = 'B'
    elif 70 <= avg:
        grade = 'C'
    elif 60 <= avg:
        grade = 'D'
    else:
        grade = 'F'

    return grade


print(get_grade(58, 62, 70))
