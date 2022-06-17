
"""
# Exercício_022
nome = str(input("\n\nDigite o seu nome completo: "))
print("O seu nome com todas as letras maiúscolas:", nome.upper())
print("O seu nome com todas as letrras minúscolas:", nome.lower())
print("A quantidade de letras que o seu nome tem sem contar os espaços: ", len(nome))
dividido = nome.split()
print("A quantidade de letras que o primeiro nome tem é: ", len(dividido[0]))
"""


"""
# Exercício 023
num = str(input("\nDigite um valor que contém 4 digitos: "))
print(num[3], 'Unidade/es')
print(num[2], 'Dezena/as')
print(num[1], 'Centena/as')
print(num[0], 'Milhar/es')
"""


# Exercício 024
cidade = str(input("Digite o nome de qualquer cidade: "))
print('Santo' in cidade[4])
