# ATIVIDADE 2
# Objetivo: trabalhar WHILE, IF, ELIF e ELSE.


# Cria a variável opcao com valor inicial zero.
opcao = 0


# Continua executando enquanto a opção escolhida for diferente de 3.
while opcao != 3:

    # Exibe o título do menu.
    print("\n--- MENU PRINCIPAL ---")

    # Exibe a primeira opção.
    print("1 - Cadastrar novo usuário")

    # Exibe a segunda opção.
    print("2 - Listar usuários")

    # Exibe a opção de encerramento.
    print("3 - Sair")


    # Solicita uma opção e converte o valor digitado para inteiro.
    opcao = int(input("Digite uma opção: "))


    # Verifica se o usuário escolheu a opção 1.
    if opcao == 1:

        # Solicita o nome da pessoa.
        nome = input("Digite o nome: ")

        # Solicita a idade e converte para inteiro.
        idade = int(input("Digite a idade: "))

        # Informa que os dados foram recebidos.
        print("Usuário cadastrado.")

        # Exibe o nome digitado.
        print("Nome:", nome)

        # Exibe a idade digitada.
        print("Idade:", idade)


    # Verifica se a opção escolhida foi 2.
    elif opcao == 2:

        # Nesta etapa ainda não existe armazenamento dos usuários.
        print("A listagem será implementada na próxima atividade.")


    # Verifica se a opção escolhida foi 3.
    elif opcao == 3:

        # Informa que o programa será encerrado.
        print("Encerrando o sistema...")


    # Executa quando nenhuma das opções anteriores foi escolhida.
    else:

        # Informa que o número informado não pertence ao menu.
        print("Opção inválida.")


# Esta mensagem aparece quando o WHILE termina.
print("Programa finalizado.")