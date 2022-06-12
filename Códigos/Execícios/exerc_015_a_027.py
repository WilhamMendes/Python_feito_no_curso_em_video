import math

"""
# Exercício 016
num = float(input("Digete um número real: "))
print("\nO número {} tem a parte interira {}\n\n" .format(num, math.trunc(num)))
"""


"""
# Exercício 017
cat_opos = float(input("\nInforme o comprimento do cateto oposto: "))
cat_adja = float(input("Informe o comprimento do cateto adjacente: "))

#hipo = (cat_opos**2) + (cat_adja**2)
hipo = math.hypot(cat_opos, cat_adja)

print("\n\nComo a hipotenusa = cateto_Oposto^2 + cateto_adjacente^2, temos que:")
print("Hipotenusa  = {:.2f} + {:.2f}" .format(cat_opos**2, cat_adja**2))
print("A hipotenusa é: {:.2f}\n\n" .format(hipo))
"""




"""
# Exercício 018
angulo = int(input("Informe o angulo? "))
print("\n Cos({}) = {:.2}\n Sen({}) = {:.2f}\n Tg({}) = {:.2}" .format(angulo, math.cos(math.radians(angulo)), angulo, math.sin(math.radians(angulo)), angulo, math.tan(math.radians(angulo))))
"""




"""
# Exercício 019
from random import choice

nom_1 = str(input("\n\nQual é o nome do 1º aluno? "))
nom_2 = str(input("Qual é o nome do 2º aluno? "))
nom_3 = str(input("Qual é o nome do 3º aluno? "))
nom_4 = str(input("Qual é o nome do 4º aluno? "))

alunos = [nom_1, nom_2, nom_3, nom_4]

print(type(alunos))
print("\nEntre os quatro alunos, o escolhido é o/a {}.\n" .format(choice(alunos)))
"""




# Exercício 020
from random import shuffle

nom_1 = str(input("\n\nQual é o nome do 1º aluno? "))
nom_2 = str(input("Qual é o nome do 2º aluno? "))
nom_3 = str(input("Qual é o nome do 3º aluno? "))
nom_4 = str(input("Qual é o nome do 4º aluno? "))

alunos = [nom_1, nom_2, nom_3, nom_4]

shuffle(alunos)
print("\nEis a ordem da apresentação dos trabalhos: ")

for aluno in alunos:
    print(aluno)

