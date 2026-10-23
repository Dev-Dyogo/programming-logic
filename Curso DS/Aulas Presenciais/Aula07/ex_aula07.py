# ATIVIDADE 7
# Estrutura de dados: Fila (Queue)
# Princípio: FIFO (First In, First Out)
# Objetivo: Implementar a estrutura de Fila.

posicoes = 25

fila = [None] * posicoes

def vazia(fila):
    return fila[0] is None

def cheia(fila):
    return fila[posicoes - 1] is not None

def adicionar(fila, nome):
    if cheia(fila):
        print('\nAtenção! Fila cheia, não é possível adicionar mais pessoas.')
        return

    for list_add in range(posicoes):
        if fila[list_add] is None:
            fila[list_add] = nome
            print('\nPessoa adicionada com sucesso à fila!')
            return

def remover(fila):
    if vazia(fila):
        print('\nAtenção! Fila vazia, não há ninguém para remover.')
        return None

    nome = fila[0]

    for list_r in range(posicoes - 1):
        fila[list_r] = fila[list_r + 1]

    fila[posicoes - 1] = None

    print('\nPessoa atendida:', nome)

    return nome

def limpar(fila):
    if vazia(fila):
        print('\nA fila já está vazia!')
        return

    while not vazia(fila):
        remover(fila)

    print('\nFila limpa com sucesso!')

def listar(fila):
    if vazia(fila):
        print('\nFila vazia!')
        return

    print('\nPessoas na fila:')

    for list_p in range(posicoes):
        if fila[list_p] is not None:
            print(f'{list_p + 1}º - {fila[list_p]}')

def exibir_menu():
    print('\n' + '_' * 40)
    print('\n[ MENU PRINCIPAL ]')
    print('\nDigite o número de uma das opções abaixo:\n')
    print('_' * 40)
    print('\n1 -> Adicionar pessoa')
    print('2 -> Remover pessoa')
    print('3 -> Limpar fila')
    print('4 -> Listar fila')
    print('5 -> Verificar se a fila está vazia')
    print('6 -> Encerrar sistema')
    print('_' * 40)

opcao = 0

while opcao != 6:

    exibir_menu()

    while True:
        opcao = input('\nDigite uma opção: ')

        if opcao.isdigit() and 1 <= int(opcao) <= 6:
            opcao = int(opcao)
            break
        else:
            print('\nAtenção! Digite um número entre 1 e 6.')

    if opcao == 1:
        nome = input('\nDigite o nome da pessoa: ')

        if nome.strip() == '':
            print('\nAtenção! Nome inválido.')
        else:
            adicionar(fila, nome)

    elif opcao == 2:
        remover(fila)

    elif opcao == 3:
        limpar(fila)

    elif opcao == 4:
        listar(fila)

    elif opcao == 5:
        if vazia(fila):
            print('\nA fila está vazia.')
        else:
            print('\nA fila não está vazia.')

    elif opcao == 6:
        print('\nEncerrando o sistema...')
