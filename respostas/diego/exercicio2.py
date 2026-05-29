verificar_aprovacao =int(input("Digite a media do aluno: "))


if verificar_aprovacao>=60:
    print("Aprovado!")

elif verificar_aprovacao>=40:
    print("Recuperação")

else:
    print("Reprovado")