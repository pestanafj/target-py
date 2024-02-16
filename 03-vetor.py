# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora,
# faça um programa, na linguagem que desejar, que calcule e retorne:
# 	• O menor valor de faturamento ocorrido em um dia do mês;
# 	• O maior valor de faturamento ocorrido em um dia do mês;
# 	• Número de dias no mês em que o valor de faturamento diário foi superior
# à média mensal.

faturamento_diario = [
    180,
    190,
    185,
    200,
    210,
    205,
    220,
    230,
    225,
    240,
    50,
    60,
    45,
    55,
    70,
    80,
    75,
    90,
    85,
    100,
    110,
    95,
    120,
    130,
    125,
    140,
    150,
    145,
    160,
    170,
    165,
]


def menor_faturamento(faturamento_diario):
    return min(faturamento_diario)


def maior_faturamento(faturamento_diario):
    return max(faturamento_diario)


def media_faturamento(faturamento_diario):
    return sum(faturamento_diario) / len(faturamento_diario)


def dias_abaixo_media(faturamento_diario):
    media = media_faturamento(faturamento_diario)
    dias_abaixo_media = 0

    for dia in faturamento_diario:
        if dia < media:
            dias_abaixo_media += 1

    return dias_abaixo_media


print(f"Faturamento diário mínimo: {menor_faturamento(faturamento_diario)}")

print(f"Faturamento diário máximo: {maior_faturamento(faturamento_diario)}")

print(f"Dias Abaixo da Média: {dias_abaixo_media(faturamento_diario)}")
