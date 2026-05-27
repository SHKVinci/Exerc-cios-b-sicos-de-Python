print("Olá, pessoal! Esses são alguns exercícios básicos que construí com Python a fim de exercitar meu coding.")

while True:
    print("Menu")
    print("Digite 1 para exercício de Calculadora Simples")
    print("Digite 2 para exercício de Verificador de n° Par ou Ímpar")
    print("Digite 3 para exercício de Verificador de Maior Número")
    menu = int(input("Digite aqui qual dos exercícios você deseja iniciar ou digite 0 para finalizar a operação: "))
    if menu == 1:
        valor1 = int(input("Digite aqui o primeiro número:"))
        valor2 = int(input("Digite aqui o segundo número:"))

        print("O resultado da soma é:", valor1 + valor2 )
        print("O resultado da divisão é:", valor1 / valor2 )
        print("O resultado da multiplicação é:", valor1 * valor2 )
        print("O resultado da subtração é:", valor1 - valor2 )

    elif menu == 2:
        valor_Usuario = int(input("Digite aqui o seu n° inteiro e eu direi se ele é impar ou par: "))
        if valor_Usuario % 2 == 0:
            print("Valor é par!")
        else:
            print("Valor é ímpar!")

    elif menu == 3:
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
    elif menu == 0:
        break
    else:
        print("Número inválido, tente novamente.")
