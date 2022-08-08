

"""
# Exercício 028
from random import Random
import random

print("\nOlá, vamos fazer um joginho. \nVocê tem que digitar um número inteiro de 0 a 5, para verificar se é o mesmo número que o computador escolheu.\n")
digite = int(input("Digite um numero inteiro de 0 a 5: "))
num_escolhido = random.randint(0, 5)

if digite == num_escolhido:
    print("PARABÉNS, Você venceu.")
else:
    print("Infelizmente você perdeu.\nOnúmero escolhido pelo computador é: {}" .format(num_escolhido))
"""


"""
# Exercício 029
veloc = float(input("\n\nInforme a velocidade do carro: "))
if veloc > 80:
    print("Você foi multado, pois o limite da velocidade estipulado é 80 km/h.")
    multa = (veloc - 80) * 7
    print("A sua multa é de {:.2f} reais.\n" .format(multa))
"""


"""
# Exercício 030
num = int(input("Digite um numero inteiro para verificar se é par ou não: "))
if (num % 2) == 0:
    print("O número {} é par!" .format(num))
else:
    print("O número {} é ímpar!" .format(num))
"""

"""
# Exercício 031
distancia = float(input("\n\nInforme a distância da sua viagem em km: "))
if distancia <= 200:
    preco = distancia * 0.50
    print("Você vai pagar {} reais." .format(preco))
else:
    preco = distancia * 0.45
    print("Você vai pagar {} reais." .format(preco))
"""


"""
# Exercício 032
ano = int(input("\nInformee um ano qualquer: "))
if (ano % 4) == 0:
    print("O ano {} é bissexto, pois é divisível por quatro.\n" .format(ano))
"""
    
# Exercício 033
n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))
n3 = int(input("Digite o 3º valor: "))
print("Verificando qual é o maior.")
