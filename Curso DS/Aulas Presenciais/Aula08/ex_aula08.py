# ATIVIDADE 8
# Objetivo: Implementar uma função capaz de ordenar um vetor de números inteiros em ordem crescente utilizando o algoritmo BubbleSort.


def bubble_sort(vetor):

    # Quantidade de vezes que o vetor será pecorido.
    for passagem in range(len(vetor)):

        # Percorre os elementos que ainda precisam ser comparados.
        for posicao_index in range(len(vetor) - 1 - passagem):

            # Verifica se o elemento atual é maior que o próximo.
            if vetor[posicao_index] > vetor[posicao_index + 1]:

                # Troca os dois elementos de posição.
                vetor[posicao_index], vetor[posicao_index + 1] = \
                vetor[posicao_index + 1], vetor[posicao_index]

# Retorna o vetor depois de ordenado.
    return vetor


# Vetor com os 20 números.
vetor_numeros = [1, 7, 10, 9, 2, 3, 20, 18, 33, 90, 44, 34, 30, 21, 27, 5, 8, 99, 54, 68]

# Mostra o vetor antes da ordenação.
print(f'Vetor original: {vetor_numeros}')

# Cria uma variável para receber o vetor ordenado, que foi retornado pelo "return" no def que foi criado.
vetor_ordenado = bubble_sort(vetor_numeros)

# Mostra o vetor depois da ordenação.
print(f'Vetor ordenado: {vetor_ordenado}')
