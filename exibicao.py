from classificacoes import classificar_carga, classificar_revisao, verificar_consumo


def exibir_ficha(modelo, dados):
    quilometragem, consumo, capacidade = dados
    print(f"\nModelo/placa: {modelo}")
    print(f"Quilometragem: {quilometragem} km")
    print(f"Consumo medio: {consumo:.2f} km/L")
    print(f"Capacidade de carga: {capacidade:.2f} kg")
    print(f"Classificacao de revisao: {classificar_revisao(quilometragem)}")
    print(classificar_carga(capacidade))
    aviso = verificar_consumo(consumo)
    if aviso:
        print(aviso)


def listar_veiculos(modelos, dados):
    print("\n--- Frota cadastrada ---")
    for i in range(len(modelos)):
        exibir_ficha(modelos[i], dados[i])
