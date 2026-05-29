numeros = []

for i in range(5):
    numero = int(input("Digite um número inteiro: "))
    numeros.append(numero)

def maior_numero(lista):
    return max(lista)

print(f"O maior valor da lista é: {maior_numero(numeros)}")