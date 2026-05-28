nome = input("digite seu nome: ") 
nota1 = float(input("digite a primeira nota: "))
nota2 = float(input("digite a segunda nota: "))

def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

media_final = calcular_media(nota1, nota2)
print(f"{nome}, sua média é: {media_final:.2f}")