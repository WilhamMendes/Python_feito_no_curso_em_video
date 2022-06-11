
"""
# Exercício 005
valor = int(input("\nEntre com um valor: "))
print(" Você digitou o número: {}\n O Antecessor de {} é: {}\n O sucessor de {} é: {}".format(valor, valor, valor-1, valor, valor+1))

# Exercício 006
print("\n O dobro de {} é: {}\n O triplo de {} é: {}\n O quadrado de {} é: {}" .format(valor, valor * 2, valor, valor * 3, valor, valor ** 2))
"""

"""
# Exercício 007
nota1 = float(input("\nEntre com a primeira nota: "))
nota2 = float(input("Entre com a senda nota: "))

media = (nota1 + nota2)/2

print("\nA média deste aluno é: {}\n" .format(media))
"""


"""
# Exercício 008
medida = float(input("Informe a medida em metro: "))
cm = medida * 100
mm = medida * 1000
print("{} metros corresponde {} centimetros.\n {} metros corresponde {} milimetros.\n" .format(medida, cm, medida, mm))
"""

"""
# Exercício 009
num = int(input("\nDigite um valor inteiro: "))
print("\nA tabuda de {}" .format(num))

print(" {} x 1 = {}\n {} x 2 = {}\n {} x 3 = {}" .format(num, num * 1, num, num * 2, num, num * 3))
print(" {} x 4 = {}\n {} x 5 = {}\n {} x 6 = {}" .format(num, num * 4, num, num * 5, num, num * 6))
print(" {} x 7 = {}\n {} x 8 = {}\n {} x 9 = {}\n {} x 10 = {}" .format(num, num * 7, num, num * 8, num, num * 9, num, num * 10))
"""


"""
# Exercício 10
from queue import PriorityQueue


dinheiro_reais = float(input("Quanto é que você tem na carteira? "))
# Como US$ 1.00 = R$3.27
diheiro_dollares = (1.00 * dinheiro_reais)/3.27
print("\nDe acordo com o dinehro que você tem '{} Rais', você pode comprar {:.3f} Dolares US.\n" .format(dinheiro_reais, diheiro_dollares))
"""


"""
# Exercício 11
altu = float(input("Qual é a altura da parede? "))
largu = float(input("Qual é a largura da parede? "))

area = altu * largu
tinta = (1 * area)/2

print("\nA área dessa parede é de {} m^2. \nSabendo que: 1 litro de tinte pinta uma área de 2 m^2, logo: " .format(area))
print("Precisamos de {} litros de tinta para pintar uma parede de {} m^2\n\n" .format(tinta, area))
"""


