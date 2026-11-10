from cadastro import cadastrar_veiculos
from busca import buscar_veiculo
from exibicao import listar_veiculos
from menu import ler_opcao
from ordenacao import ordenar_veiculos


def main():
    modelos = [""] * 5
    # Cada linha: quilometragem, consumo medio e capacidade de carga.
    dados = [[0, 0.0, 0.0] for _ in range(5)]
    cadastrar_veiculos(modelos, dados)

    opcao = ""
    while opcao != "0":
        opcao = ler_opcao()
        match opcao:
            case "1":
                listar_veiculos(modelos, dados)
            case "2":
                ordenar_veiculos(modelos, dados)
            case "3":
                buscar_veiculo(modelos, dados)
            case "0":
                print("Programa encerrado.")
            case _:
                print("Opcao invalida. Escolha 0, 1, 2 ou 3.")


if __name__ == "__main__":
    main()
