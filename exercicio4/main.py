def adicionar_contato(agenda):
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")

def buscar_contato(agenda):
    nome = input("Digite o nome do contato que deseja buscar: ")
    if nome in agenda:
        print(f"Telefone de {nome}: {agenda[nome]}")
    else:
        print("Contato não encontrado.")

def remover_contato(agenda):
    nome = input("Digite o nome do contato que deseja remover: ")
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado.")



while True:
    print("Menu")
    print("Digite 1 para exercício de Agenda de contatos")
    print("Digite 2 para exercício de Frequência de Palavras")
    print("Digite 3 para exercício de Filtrando Dados")
    menu = int(input("Digite aqui qual dos exercícios você deseja iniciar ou digite 0 para finalizar a operação: "))
    if menu == 1:
            agenda = {}
            while True:
                print("Menu da Agenda de Contatos")
                print("Digite 1 para adicionar um contato")
                print("Digite 2 para buscar um contato")
                print("Digite 3 para remover um contato")
                print("Digite 4 para listar todos os contatos")
                print("Digite 0 para voltar ao menu principal")
                escolha = int(input("Digite aqui a sua escolha: "))
                if escolha == 1:
                    adicionar_contato(agenda)
                elif escolha == 2:
                    buscar_contato(agenda)
                elif escolha == 3:
                    remover_contato(agenda)
                elif escolha == 0:
                    break
                elif escolha == 4:
                    if agenda:
                        print("Contatos na agenda:")
                        for nome, telefone in agenda.items():
                            print(f"{nome}: {telefone}")
                    else:
                        print("A agenda está vazia.")
                else:
                    print("Número inválido, tente novamente.")

    elif menu == 2:
        texto = input("Digite um texto: ")
        palavras = texto.split()
        frequencia = {}
        for palavra in palavras:
            if palavra in frequencia:
                frequencia[palavra] += 1
            else:
                frequencia[palavra] = 1
        print("Frequência das palavras:")
        for palavra, contagem in frequencia.items():
            print(f"{palavra}: {contagem}")

    elif menu == 3:
        print("Exercício de Filtrando Dados")
        lista = [ 15, 22, 8, 34, 17, 45, 12, 28]
        idade_minima = int(input("Digite a idade mínima para filtrar: "))
        lista_filtrada = [idade for idade in lista if idade >= idade_minima]
        print(f"Idades filtradas (maiores ou iguais a {idade_minima}): {lista_filtrada}")
    elif menu == 0:
        break
    else:
        print("Número inválido, tente novamente.")