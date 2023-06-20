import os

def clear_terminal():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')

def merge_count(esq, direita):
    merged = []
    count = 0
    i, j = 0, 0

    while i < len(esq) and j < len(direita):
        if esq[i] <= direita[j]:
            merged.append(esq[i])
            i += 1
        else:
            merged.append(direita[j])
            count += len(esq) - i
            j += 1

    merged.extend(esq[i:])
    merged.extend(direita[j:])
    return merged, count

def merge_sort_count(notas):
    if len(notas) <= 1:
        return notas, 0

    mid = len(notas) // 2
    esq, countEq = merge_sort_count(notas[:mid])
    direita, countD = merge_sort_count(notas[mid:])
    merged, countED = merge_count(esq, direita)

    return merged, countEq + countD + countED


clear_terminal()

print("=================================================================================================================================================================================")
print("Olá, e seja muito bem vindo ao analisador de gostos musicais!, o nosso objetivo é analisar seus gostos musicais como um apreciador de ROCK.\nDiga abaixo uma nota de 1 a 5 para as cinco bandas abaixo e nós diremos o quão próximo você é das nossas previsões.")
print("=================================================================================================================================================================================\n\n")

notas = []
bandas =[ 'Kondzilla', 'Backstreet Boys','Exalta Samba','Aerosmith', 'Black Sabbath']
for i in range(5):
    nota = int(input(f"Digite a sua nota para {bandas[i]}: "))
    notas.append(nota)

sorted_notas, inversions = merge_sort_count(notas)
clear_terminal()

if inversions <= 2:
    print("Uau! você realmente é do rock! Seus gostos são muito próximos dos nossos registros!\nContinue assim!")
if inversions > 2 and inversions < 5:
    print("Seus gostos são mais variados do que esperávamos, mas claramente rock ainda te agrada.\nContinue assim!")
if inversions > 5:
    print("Um...Wow, você não curte rock mesmo.\nBom, acho que cada um tem seu gosto.")
