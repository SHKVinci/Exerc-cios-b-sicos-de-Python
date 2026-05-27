## Palíndromo: Escreva uma função que recebe uma palavra e retorna True se ela for um palíndromo (ex: "arara", "radar").
## Contagem de vogais: Dada uma string, conte quantas vogais ela tem.
## Calculadora com funções: Refaça a calculadora do exercício 2 do nível 1, mas desta vez cada operação deve ser uma função separada.
## Jogo de adivinhação: O programa sorteia um número de 1 a 20. O usuário tem 5 tentativas para adivinhar. A cada erro, diga se o número é maior ou menor.

import random

def palindromo(palavra):
    if palavra == palavra[::-1]:
        return True
    else:
        return False
        
def soma(numero1, numero2):
    resultado1 = numero1 + numero2
    return resultado1
def subtracao(numero1, numero2):
    resultado2 = numero1 - numero2
    return resultado2
def multiplicacao(numero1, numero2):
    resultado3 = numero1 * numero2
    return resultado3
def divisao(numero1, numero2):
    resultado4 = numero1 / numero2
    return resultado4

while True:
    print("Menu")
    print("Digite 1 para exercício de Palíndromo")
    print("Digite 2 para exercício de Contagem de Vogais")
    print("Digite 3 para exercício de Calculadora com funções")
    print("Digite 4 para exercício de Jogo de adivinhação")
    menu = int(input("Digite aqui qual dos exercícios você deseja iniciar ou digite 0 para finalizar a operação: "))
    if menu == 1:
        palavra_digitada = input("Digite aqui a palavra que você gostaria de saber se é um Palíndromo: ")
        resultado = palindromo(palavra_digitada)
        if resultado == True:
            print("A palavra é um palíndromo!!")
        else:
            print("A palavra não é um palíndromo.")
    elif menu == 2:
        palavra = input("Digite aqui a palavra que você deseja realizar a contagem de vogais: ")
        contagem = 0
        for letra in palavra:
            if letra in "aeiou":
                contagem = contagem + 1
        if contagem != 0:
            print("A palavra digitada tem: ", contagem, "vogais")
        else:
            print("A palavra digitada não tem nenhuma vogal.")

    elif menu == 3:
        numero_digitado1 = float(input("Digite aqui o primeiro n°: "))
        operacao = input("Para multiplicar use o *, para somar use o +, para subtrair use o - e dividir use o /: ")
        numero_digitado2 = float(input("Digite aqui o segundo n°: "))
        if operacao == "*":
            print("O resultado é: ", multiplicacao(numero_digitado1,numero_digitado2) )
        elif operacao == "/" and numero_digitado2 == 0:
            print("Impossível fazer esta operação.")
        elif operacao == "/" and numero_digitado2 != 0:
            print("O resultado é: ", divisao(numero_digitado1,numero_digitado2) )
        elif operacao == "-":
            print("O resultado é: ", subtracao(numero_digitado1,numero_digitado2) )
        elif operacao == "+":
            print("O resultado é: ", soma(numero_digitado1,numero_digitado2) )
        else:
            print("Operação desconhecida... Por favor, digite a operação conforme a instrução manda.")
    elif menu == 4:
        numero_sorteado = random.randint(1, 20)
        tentativas = 5
        while tentativas > 0:
            palpite = int(input("Digite seu palpite (1-20): "))
            if palpite == numero_sorteado:
                print("Parabéns! Você acertou.")
                break
            elif palpite < numero_sorteado:
                print("O número é maior.")
                print("Você tem mais", tentativas - 1, "tentativas.")
            else:
                print("O número é menor.")
                print("Você tem mais", tentativas - 1, "tentativas.")
            tentativas -= 1
        if tentativas == 0:
            print("Você perdeu! O número era:", numero_sorteado)
    elif menu == 0:
        break
    else:
        print("Número inválido, tente novamente.")