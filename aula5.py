
numero = int(input("Digite um numero: "))

while numero != -1:
    if (numero>=10):
        indice = 1
        for indice in range(1,numero+1):
            if (numero%indice==0):
                print(indice)

    else:
        print("Numero invalido")
        break

    numero = int(input("Digite um numero ou -1 para sair: "))

print("Sair do While")