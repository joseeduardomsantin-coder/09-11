from exibicao import exibir_ficha
from ordenacao import ordenar_veiculos


def buscar_veiculo(modelos, dados):
    ordenar_veiculos(modelos, dados)
    procurado = input("Digite o modelo ou placa para buscar: ").strip().casefold()
    inicio = 0
    fim = len(modelos) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        atual = modelos[meio].casefold()
        if atual == procurado:
            exibir_ficha(modelos[meio], dados[meio])
            return
        if atual < procurado:
            inicio = meio + 1
        else:
            fim = meio - 1

    print("Veiculo nao encontrado.")
