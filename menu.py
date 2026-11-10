def mostrar_menu():
    print("\n=== Cadastro e Logistica da Frota ===")
    print("1 - Listar veiculos")
    print("2 - Ordenar veiculos por modelo/placa")
    print("3 - Pesquisar veiculo")
    print("0 - Sair")


def ler_opcao():
    mostrar_menu()
    return input("Escolha uma opcao: ").strip()
