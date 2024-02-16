# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# 	a) Essa string pode ser informada através de qualquer entrada
# de sua preferência ou pode ser previamente definida no código;
# 	b) Evite usar funções prontas, como, por exemplo, reverse;


def reverter_string(string):

    string_vetor = "".join(string)

    posicao = len(string_vetor) - 1

    string_vetor_reverso = []

    while posicao >= 0:
        string_vetor_reverso.append(string[posicao])
        posicao -= 1

    string_reversa = "".join(map(str, string_vetor_reverso))

    return string_reversa


string = input("Informe string que deseja inverter: ")
print(f"String Invertida: {reverter_string(string)}")
