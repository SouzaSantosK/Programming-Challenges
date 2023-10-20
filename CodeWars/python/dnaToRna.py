# O ácido desoxirribonucléico, DNA, é a principal molécula de armazenamento de informações em sistemas biológicos. É composto por quatro bases de ácido nucleico Guanina ('G'), Citosina ('C'), Adenina ('A') e Timina ('T').

# O ácido ribonucleico, RNA, é a principal molécula mensageira nas células. O RNA difere ligeiramente do DNA em sua estrutura química e não contém timina. No RNA, a timina é substituída por outro ácido nucléico Uracil ('U').

# Crie uma função que traduza uma determinada sequência de DNA em RNA.

# Por exemplo:
# "GCAT"  =>  "GCAU"
# A string de entrada pode ter comprimento arbitrário - em particular, pode estar vazia. Todas as entradas são garantidas como válidas, ou seja , cada string de entrada consistirá apenas em 'G', e/ou .'C''A''T'

# Minha resolução
def dna_to_rna(dna):
    return dna.replace('T', 'U')


print(dna_to_rna('GCAT'))
