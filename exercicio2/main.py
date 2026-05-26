while True:
    print("Menu")
    print("Digite 1 para exercício de Contagem Regressiva")
    print("Digite 2 para exercício de Soma e Média de valores em lista")
    print("Digite 3 para exercício de contagem FizzBuzz")
    print("Digite 4 para exercício de contagem Tabuada")
    menu = int(input("Digite aqui qual dos exercícios você deseja iniciar ou digite 0 para finalizar a operação: "))
    if menu == 1:
        print("Exercício de contagem regressiva")
        from time import sleep
        valor1 = int(input("Digite qualquer número para iniciar a contagem regressiva até o 0: "))
        for valor1 in range(valor1, -1, -1):
            print(valor1)
            sleep(1)
    elif menu == 2:
        print("Exercício de soma e média dos valores em lista")
        val1 = int(input("Digite o primeiro valor: "))
        val2 = int(input("Digite o segundo valor: "))
        val3 = int(input("Digite o terceiro valor: "))
        val4 = int(input("Digite o quarto valor: "))
        val5 = int(input("Digite o quinto valor: "))
        lista_valores = [val1, val2, val3, val4, val5]
        print("Os n° digitados foram: ", lista_valores)
        total = 0
        contagem = 0
        for numero in lista_valores:
            total = total + numero
            contagem = contagem + 1 
        print("A soma total dos n° é: ", total)
        media = total / contagem
        print("A média dos n° é: ", media)
    elif menu == 3:
        print("Exercício Fizzbuzz")
        for numero1 in range(1, 31):
            if numero1 % 3 == 0 and numero1 % 5 == 0:
                print(numero1, "= Fizzbuzz")
            elif numero1 % 3 == 0:
                print( numero1, "= Fizz")
            elif numero1 % 5 == 0:
                print( numero1, "= Buzz")
            else:
                print(numero1)
    elif menu == 4:
        print("Exercício da tabuada")
        numero2 = int(input("Digite aqui o n° que você quer saber a tabuada: "))
        for numero4 in range(1, 11):
            tabuada = numero4 * numero2
            print(numero2, "x", numero4, "=", tabuada)
    elif menu == 0: 
        print("Operação finalizada")
        break
    else:
        print("Número inválido, tente novamente.")


    
