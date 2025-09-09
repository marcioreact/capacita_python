a = int(input("Digite um angulo: "))
b = int(input("Digite um angulo: "))
c = int(input("Digite um angulo: "))


if(a+b+c==180):
    if a == b == c:
        print("equilatero")
    elif a == b or a == c or b == c:
        print("isosceles")
    else:
        print("escaleno")
else:
    print("Não é um triangulo")
    