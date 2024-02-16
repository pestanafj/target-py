# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor
# sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...),
# escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência
# de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.


def pertence_fibonacci(numero_recebido):
    fibonacci = [0, 1]
    tamanho_sequencia = 2
    novo_numero = 1

    while novo_numero < numero_recebido:
        novo_numero = (
            fibonacci[tamanho_sequencia - 2] + fibonacci[tamanho_sequencia - 1]
        )
        fibonacci.append(novo_numero)
        tamanho_sequencia += 1

    if numero_recebido in fibonacci:
        index = fibonacci.index(numero_recebido)
        print(
            f"O número {numero_recebido} é o {index+1}º numero da sequencia de Fibonacci!"
        )
    else:
        print(f"O número {numero_recebido} não pertence à sequencia de Fibonacci!")


numero_recebido = int(input("Informe numero a ser verificado:"))
pertence_fibonacci(numero_recebido)
