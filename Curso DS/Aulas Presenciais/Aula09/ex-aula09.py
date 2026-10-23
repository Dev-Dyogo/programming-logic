# ATIVIDADE 9
# Objetivo: Implementar um algoritmo de ordenação utilizando o método MergeSort.

def merge_sort(vetor):

# Verifica se o vetor possui mais de um elemento.
    if len(vetor) > 1:

# Encontra o ponto central do vetor.
        meio = len(vetor) // 2

# Divide o vetor em duas partes.
        esquerda = vetor[:meio]
        direita = vetor[meio:]

# Chama a função novamente para ordenar a parte esquerda.
        esquerda = merge_sort(esquerda)

# Chama a função novamente para ordenar a parte direita.
        direita = merge_sort(direita)

# Variáveis utilizadas para percorrer as duas partes.
        posicao_esquerda = 0
        posicao_direita = 0
        posicao_vetor = 0

# Compara os elementos das duas partes e coloca o menor elemento no vetor.
        while posicao_esquerda < len(esquerda) and posicao_direita < len(direita):

            if esquerda[posicao_esquerda] < direita[posicao_direita]:

                vetor[posicao_vetor] = esquerda[posicao_esquerda]
                posicao_esquerda += 1

            else:

                vetor[posicao_vetor] = direita[posicao_direita]
                posicao_direita += 1

            posicao_vetor += 1

# Adiciona os elementos que ainda estão na parte esquerda.
        while posicao_esquerda < len(esquerda):

            vetor[posicao_vetor] = esquerda[posicao_esquerda]
            posicao_esquerda += 1
            posicao_vetor += 1

# Adiciona os elementos que ainda estão na parte direita.
        while posicao_direita < len(direita):

            vetor[posicao_vetor] = direita[posicao_direita]
            posicao_direita += 1
            posicao_vetor += 1

# Retorna o vetor depois de ordenado.
    return vetor


# Vetor com os 20 números.
vetor_numeros = [1, 7, 10, 9, 2, 3, 20, 18, 33, 90, 44, 34, 30, 21, 27, 5, 8, 99, 54, 68]

# Mostra o vetor antes da ordenação.
print(f'Vetor original: {vetor_numeros}')

# Cria uma variável para receber o vetor ordenado.
vetor_ordenado = merge_sort(vetor_numeros)

# Mostra o vetor depois da ordenação.
print(f'Vetor ordenado: {vetor_ordenado}')