idade = 0
idade = int(input("digite a idade: "))
if idade < 16:
    print("Não pode votar")
elif idade >= 18 and idade < 70:
    print("obrigatório")
else:
    print("Facultativo")