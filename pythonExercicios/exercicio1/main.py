print("Olá, pessoal! Esse são alguns exercícios básicos que construí com Python a fim de exercitar meu coding.")

resposta = int(input("Você quer fazer o primeiro exercício? Se sim, digite 1. Caso contrário, digite 2. Digite aqui: "))
if resposta == 1:
    valor1 = int(input("Digite aqui o primeiro número:"))
    valor2 = int(input("Digite aqui o segundo número:"))

    print("O resultado da soma é:", valor1 + valor2 )
    print("O resultado da divisão é:", valor1 / valor2 )
    print("O resultado da multiplicação é:", valor1 * valor2 )
    print("O resultado da subtração é:", valor1 - valor2 )

resposta2 = int(input("Você quer fazer o segundo exercício? Se sim, digite 1. Caso contrário, digite 2. Digite aqui: "))
if resposta2 == 1:
    valor_Usuario = int(input("Digite aqui o seu n° inteiro e eu direi se ele é impar ou par: "))
    if valor_Usuario % 2 == 0:
        print("Valor é par!")
    else:
        print("Valor é ímpar!")

resposta3 = int(input("Você quer fazer o terceiro exercício? Se sim, digite 1. Caso contrário, digite 2. Digite aqui: "))
if resposta3 <= 1:
    print("Digite três valores e eu direi qual deles é o maior")
    val1 = int(input("Digite o primeiro valor: "))
    val2 = int(input("Digite o segundo valor: "))
    val3 = int(input("Digite o terceiro valor: "))
    if val1 > val2 and val1 > val3:
        print("O n° ",  val1, "é o maior n°")
    elif val2 > val1 and val2 > val3:
        print("O n° ", val2, "é o maior n°")
    else:
        print("O n° ", val3, "é o maior n°")