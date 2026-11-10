def ordenar_veiculos(modelos, dados):
    # Bubble Sort; cada troca do modelo/placa tambem move seus dados.
    for i in range(len(modelos) - 1):
        houve_troca = False
        for j in range(len(modelos) - 1 - i):
            if modelos[j].casefold() > modelos[j + 1].casefold():
                modelos[j], modelos[j + 1] = modelos[j + 1], modelos[j]
                dados[j], dados[j + 1] = dados[j + 1], dados[j]
                houve_troca = True
        if not houve_troca:
            break
    print("\nVeiculos ordenados alfabeticamente.")
