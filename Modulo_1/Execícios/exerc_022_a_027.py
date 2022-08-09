

"""
# Exercício_022
nome = str(input("\n\nDigite o seu nome completo: "))
print("O seu nome com todas as letras maiúscolas é:", nome.upper())
print("O seu nome com todas as letras minúscolas é:", nome.lower())
print("O seu nome tem {} letras." .format(len(nome) - nome.count(" ")))
dividido = nome.split()
print("O seu primeiro nome é: {} e ele tem {} letras. " .format(dividido[0], len(dividido[0])))
"""


"""
# Exercício 023
num = str(input("\nDigite um valor que contém 4 digitos: "))
print(num[3], 'Unidade/es')
print(num[2], 'Dezena/as')
print(num[1], 'Centena/as')
print(num[0], 'Milhar/es\n\n')
"""


"""
# Exercício 023

num = int(input("\nDigite um valor que contém 4 digitos: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print("\nAnalisando o número {}" .format(num))
print('O número que você digitou tem {} Unidade/es' .format(u))
print('O número que você digi tou tem {} Dezena/as' . format(d))
print('O número que você digitou tem {} Centena/as' .format(c))
print('O número que você digitou tem {} Milhar/es\n\n' .format(m))
"""





"""
# Exercício 024
cidade = str(input("Digite o nome de qualquer cidade: ")).strip()
print(cidade[:5].upper() == 'SANTO')
"""
  


"""
#Exercício 025
nome = str(input("Qual é o seu nome completo? ")).strip()
print("Silva está no nome digitado? R: ", 'silva' in nome.lower())
"""



"""
#Exercício 026
frase = str(input("Digite uma frase: ")).strip()
frase = frase.upper()
print("A letra (A) aparece ", frase.count('A'), "vezes na frase.")
print("A letra (A) aparece pela 1ª Vez na posição {}" .format(frase.find('A')+1))
print("A letra (A) apareceu pela última vez na posição {}" .format(frase.rfind('A')+1))
"""



# Exercício 027
nome = str(input("Digite o seu nome: ")).strip()
nom = nome.split() 
print("O seu primeiro nome é: {}" .format(nom[0]))
print("O seu último nome é: {}" .format(nom[len(nom)-1]))
