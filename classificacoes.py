def classificar_revisao(quilometragem):
    if quilometragem <= 20000:
        return "Revisao Leve"
    if quilometragem <= 60000:
        return "Revisao Geral"
    return "Troca de Componentes Pesados"


def classificar_carga(capacidade):
    if capacidade > 2000:
        return "Porte: Pesado"
    return "Porte: Leve"


def verificar_consumo(consumo):
    if consumo < 6:
        return "Aviso: Alto Custo de Combustivel"
    return ""
