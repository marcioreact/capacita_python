


nome = input("Digite seu nome completo: ")
nome = nome.lower()
nome = nome.replace(" ", "")

vogais = "aeiou"
consoantes = "bcdfghjlmnpqrstvxzyw"

if nome[0] in vogais:
    print("O primeiro nome comeca com vogal")
if nome[-1] in consoantes:
    print("O ultimo nome termina com consoante")
else:
    print("neutro")


#texto = nome.split()

#print("Primeiro nome: {} -- último nome {}".format (texto[0], texto[-1]))

#print("Nome em maiúsculas:", nome.upper())

#print("Nome em minúsculas:", nome.lower())

#print("Quantidade de letras (sem espaços): {}".format(len(nome.replace(" ", ""))))
