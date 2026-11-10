def ler_modelo_ou_placa():
    modelo = input("Modelo ou placa: ").strip()
    while not modelo:
        print("O modelo ou a placa nao pode ficar vazio.")
        modelo = input("Modelo ou placa: ").strip()
    return modelo


def ler_quilometragem():
    while True:
        try:
            quilometragem = int(input("Quilometragem atual (km): "))
            if quilometragem >= 0:
                return quilometragem
            print("A quilometragem nao pode ser negativa.")
        except ValueError:
            print("Digite um numero inteiro valido.")


def ler_numero(mensagem):
    while True:
        try:
            numero = float(input(mensagem).replace(",", "."))
            if numero >= 0:
                return numero
            print("Digite um valor nao negativo.")
        except ValueError:
            print("Digite um numero valido.")
