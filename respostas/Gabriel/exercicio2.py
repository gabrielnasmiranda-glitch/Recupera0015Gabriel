aluno = input("digite o nome do aluno:")
n1 = float (input("digite a primeira nota do aluno:"))
n2 = float (input("Digite a segunda nota do aluno:"))

def calcular_media(nota1,nota2):
    return (nota1 + nota2) / 2

media = calcular_media(n1,n2)

print (f"O aluno {aluno} obteve a seguinte média: {media}")


if media >= 60:
    print (f"{aluno} Aprovado!")

if media >=40:
    print(f"{aluno} está de Recuperação!")

else: 
    print(f"{aluno} Reprovado!")