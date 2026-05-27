# Exercício 1 - Variáveis e Funções

Crie um programa em Python que:

1. Solicite o nome do aluno.
2. Solicite duas notas.
3. Crie uma função chamada calcular_media().
4. A função deve retornar a média das notas.
5. Exiba:
- nome do aluno
- média calculada

# calc notas

def calcular_media(nota1, nota2):
    media = (int(nota1) + int(nota2)) /2 
    return media 
    

n1 = input("digite a primeira nota : ")
n2 = input("digite a segunda nota : ")
nome input("digite seu nome :") 
print(calcular_media(n1, n2))
print 
