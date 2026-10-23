# ATIVIDADE 4
# Objetivo: A necessidade de realizar a busca de um usuário pelo seu nome, assim como permitir a exclusão.

def buscar_user(nome_buscado, lista_nomes, lista_idades):
    for listan in range(len(lista_nomes)):
        if lista_nomes[listan] == nome_buscado:
            print('\n>>> Usuário Encontrado <<<')
            print(f'Nome: {lista_nomes[listan]}')
            print(f'Idade: {lista_idades[listan]}')
            return listan

    return -1

def user_delet(nome_buscado, lista_nomes, lista_idades):
    posicao = buscar_user(nome_buscado, lista_nomes, lista_idades)
    if posicao != -1:
        user_delet = lista_nomes.pop(posicao)
        lista_idades.pop(posicao)
        print(f'\n Usuário "{user_delet}" excluído com sucesso!')
    else:
        print('\nAtenção! Usuário não encontrado ou não existe para exclusão.')

print('\nSeja bem-vindo(a) ao Programa para Cadastros de Usuários da Ozzy!\n')

quantidade_users = int(input('Quantos usuários deseja cadastrar?\n Digite uma quantidade maxima:'))

nomes = []

idades = []

opcao = 0

while opcao != 5:

    print('\n>>> MENU PRINCIPAL <<<\n\nDigite o n° de uma das opções abaixo:\n')

    print('1 -> Cadastrar novo usuário')

    print('2 -> Listar todos os usuários cadastrados')

    print('3 -> Buscar pelo nome de usuário')

    print('4 -> Excluir usuário')

    print('5 -> Sair')

    opcao = int(input('Digite uma opção: '))

    print('------------------------')

    if opcao == 1:

        if len(nomes) < quantidade_users:

            nome = input('Digite seu nome de usuário: ')

            idade = int(input('Digite sua idade: '))

            nomes.append(nome)

            idades.append(idade)

            print('\nUsuário cadastrado com sucesso!')

        else:

            print('\nAtenção! Limite de usuários pré-estabelecido atingido.')

    elif opcao == 2:

        if len(nomes) == 0:

            print('\nAtenção! Nenhum usuário cadastrado.')

            print('------------------------')

        else:

            print('\n>>> USUÁRIOS CADASTRADOS <<<')

            for user in range(len(nomes)):

                print('Posição:', user)

                print('Nome:', nomes[user])

                print('Idade:', idades[user])

                print('------------------------')

    elif opcao == 3:

            pesquisar_user = input('Digite o nome do usuário que deseja buscar: ')
            posicao = buscar_user(pesquisar_user, nomes, idades)

            if posicao == -1:
                print('\nAtenção! Usuário não encontrado ou não cadastrado.')

    elif opcao == 4:

            pesquisar_user = input('Digite o nome do usuário que deseja excluir: ')
            user_delet(pesquisar_user, nomes, idades)

    elif opcao == 5:

        print('Encerrando o sistema...')

    else:

        print('Atenção! Opção inválida.')

print('Programa finalizado.')
