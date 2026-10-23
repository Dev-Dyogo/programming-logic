# ATIVIDADE 6
# Estrutura de dados: Pilha (Stack)
# Princípio: LIFO (Last In, First Out)
# Objetivo: Implementar a estrutura de Pilha utilizando uma estrutura homogênea.

# Função para mostrar menu principal na tela.
def exibir_menu():
    print('_'* 30)
    print('\n[ MENU PRINCIPAL ]\n\nDigite o número de uma das opções abaixo:\n')
    print('1 -> Listar pilha de livros')
    print('2 -> Empilhar novo livro')
    print('3 -> Desempilhar livro')
    print('4 -> Retirar todos os livros')
    print('5 -> Encerrar biblioteca')
    print('_'* 30)

def listar_pilha(pilha):
# Verifica se a pilha possui pelo menos 1 elemento.
    if len(pilha) > 0:
        print(f'\nSua pilha de livros atual: {pilha}')
# O índice [-1] sempre acessa o último elemento da estrutura, que representa o "topo" da pilha.
        print(f'O livro no topo é: {pilha[-1]}')
    else:
# Mensagem de aviso caso a pilha esteja vazia.
        print('\nA pilha de livros está vazia.')

def empilhar_livro(pilha):
# Solicita o nome de um novo livro.
    novo_livro = input('Digite o nome do livro para empilhar: ')
# O método .append() adiciona o novo elemento sempre ao topo da pilha.
    pilha.append(novo_livro)
    print('\nNovo livro empilhado com sucesso ao topo da pilha.')

def desempilhar_livro(pilha):
# Antes de desempilhar, verifica se a pilha não está vazia para evitar erros.
    if len(pilha) > 0:
# O método .pop() remove e retorna o último elemento adicionado à lista (o topo).
# Isso aplica diretamente a regra LIFO (Último a entrar, primeiro a sair).
        livro_removido = pilha.pop()
        print(f'\nLivro "{livro_removido}" desempilhado com sucesso do topo da pilha.')
    else:
        print('\nNão há livros para desempilhar. A pilha está vazia.')

def esvaziar_pilha(pilha):
# O método .clear() apaga todos os elementos da lista de uma só vez.
    pilha.clear()
    print('\nTodos os livros foram retirados. A pilha está vazia.')

# INÍCIO DO PROGRAMA PRINCIPAL.

print('\nSeja bem-vindo(a) ao sistema da biblioteca de pilha.\n')

while True:
    quantidade_livros = input('Quantos livros deseja empilhar inicialmente? ')

    if quantidade_livros.isdigit():
        numeros_de_livros = int(quantidade_livros)
        break
    else:
        print('\nAtenção! Digite em números inteiros a quantidade de livros.\n')

pilha_de_livros = []

for livro in range(numeros_de_livros):
    nome_livro = input(f'\nDigite o nome do {livro+1}º livro: ')
    pilha_de_livros.append(nome_livro)

if numeros_de_livros > 0:
    print('\nLivros cadastrados com sucesso e adicionados à pilha.')

opcao = 0

while opcao != 5:
    
    exibir_menu()

    while True:
        opcao = input('\nDigite uma opção: ')

        if opcao.isdigit() and 1 <= int(opcao) <= 5:
            opcao = int(opcao)
            break
        else:
            print('\nOpção inválida! Digite apenas um número entre 1 e 5.')

   
    if opcao == 1:
        listar_pilha(pilha_de_livros)
        
    elif opcao == 2:
        empilhar_livro(pilha_de_livros)
        
    elif opcao == 3:
        desempilhar_livro(pilha_de_livros)
        
    elif opcao == 4:
        esvaziar_pilha(pilha_de_livros)
        
    elif opcao == 5:
        print('\nEncerrando o sistema da biblioteca de pilha...')