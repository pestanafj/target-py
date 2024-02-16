# 4) Dado o valor de faturamento mensal de uma distribuidora,
# detalhado por estado:
# 	SP – R$67.836,43
# 	RJ – R$36.678,66
# 	MG – R$29.229,88
# 	ES – R$27.165,48
# 	Outros – R$19.849,53
# Escreva um programa na linguagem que desejar onde calcule o percentual
# de representação que cada estado teve dentro do valor total mensal da distribuidora.


def percentual_representacao(faturamento_por_estado):
    soma = 0
    for estado in faturamento_por_estado:
        faturamento = float(
            (
                faturamento_por_estado[estado]
                .replace(".", "")
                .replace(",", ".")
                .replace("R$", "")
            )
        )
        soma += faturamento
        faturamento_por_estado[estado] = faturamento

    participacao_por_estado = {}

    for estado in faturamento_por_estado:
        participacao_por_estado[estado] = (
            str(round((faturamento_por_estado[estado] / soma) * 100, 2)) + "%"
        )

    return participacao_por_estado


faturamento_por_estado = {
    "SP": "R$67.836,43",
    "RJ": "R$36.678,66",
    "MG": "R$29.229,88",
    "ES": "R$27.165,48",
    "Outros": "R$19.849,53",
}

print(percentual_representacao(faturamento_por_estado))
