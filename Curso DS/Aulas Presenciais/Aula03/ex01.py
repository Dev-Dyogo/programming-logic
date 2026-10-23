# ATIVIDADE 3
# Objetivo: utilizar listas para armazenar vários usuários.


# Solicita a quantidade máxima de pessoas que poderão ser cadastradas.
quantidade_maxima = int(input("Quantas pessoas poderão ser cadastradas? "))


# Cria uma lista vazia para armazenar os nomes.
nomes = []


# Cria uma lista vazia para armazenar as idades.
idades = []


# Cria a variável que controlará o menu.
opcao = 0


# Mantém o programa funcionando até que seja escolhida a opção 3.
while opcao != 3:

    # Exibe o título.
    print("\n--- MENU PRINCIPAL ---")

    # Exibe a opção de cadastro.
    print("1 - Cadastrar novo usuário")

    # Exibe a opção de listagem.
    print("2 - Listar usuários")

    # Exibe a opção de saída.
    print("3 - Sair")


    # Recebe a opção escolhida.
    opcao = int(input("Digite uma opção: "))


    # Verifica se a opção de cadastro foi escolhida.
    if opcao == 1:

        # Verifica se ainda existe espaço para novos usuários.
        if len(nomes) < quantidade_maxima:

            # Solicita o nome da pessoa.
            nome = input("Digite o nome: ")

            # Solicita a idade da pessoa.
            idade = int(input("Digite a idade: "))

            # Adiciona o nome ao final da lista nomes.
            nomes.append(nome)

            # Adiciona a idade ao final da lista idades.
            idades.append(idade)

            # Informa que o cadastro foi realizado.
            print("Usuário cadastrado com sucesso.")


        # Executa quando a quantidade máxima foi atingida.
        else:

            # Informa que não existem mais posições disponíveis.
            print("Não existem mais posições disponíveis.")


    # Verifica se a opção de listagem foi escolhida.
    elif opcao == 2:

        # Verifica se não existe nenhum usuário cadastrado.
        if len(nomes) == 0:

            # Informa que a lista está vazia.
            print("Nenhum usuário cadastrado.")


        # Executa quando existem usuários.
        else:

            # Exibe um título para a listagem.
            print("\n--- USUÁRIOS CADASTRADOS ---")


            # Percorre todas as posições da lista nomes.
            for i in range(len(nomes)):

                # Exibe a posição do usuário.
                print("Posição:", i)

                # Exibe o nome armazenado naquela posição.
                print("Nome:", nomes[i])

                # Exibe a idade correspondente à mesma posição.
                print("Idade:", idades[i])

                # Exibe uma linha apenas para organização.
                print("------------------------")


    # Verifica se foi escolhida a opção de saída.
    elif opcao == 3:

        # Informa que o sistema está sendo encerrado.
        print("Encerrando o sistema...")


    # Executa caso seja digitada uma opção inexistente.
    else:

        # Mostra uma mensagem de erro.
        print("Opção inválida.")


# Mensagem apresentada após sair do WHILE.
print("Programa finalizado.")