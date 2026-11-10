from entrada import ler_modelo_ou_placa, ler_numero, ler_quilometragem


def cadastrar_veiculos(modelos, dados):
    print("\n--- Cadastro dos 5 veiculos ---")
    for i in range(len(modelos)):
        print(f"\nVeiculo {i + 1}")
        modelos[i] = ler_modelo_ou_placa()
        dados[i][0] = ler_quilometragem()
        dados[i][1] = ler_numero("Consumo medio (km/L): ")
        dados[i][2] = ler_numero("Capacidade de carga (kg): ")
    print("\nCadastro concluido.")
