import math

"""
# Exercício 016
num = float(input("Digete um número real: "))
print("\nO número {} tem a parte interira {}\n\n" .format(num, math.floor(num)))
"""


"""
# Exercício 017
cat_opos = float(input("\nInforme o comprimento do cateto oposto: "))
cat_adja = float(input("Informe o comprimento do cateto adjacente: "))

hipo = (cat_opos**2) + (cat_adja**2)

print("\n\nComo a hipotenusa = cateto_Oposto^2 + cateto_adjacente^2, temos que:")
print("Hipotenusa  = {:.2f} + {:.2f}" .format(cat_opos**2, cat_adja**2))
print("A hipotenusa é: {:.2f}\n\n" .format(hipo))
"""


# Exercício 018
angulo = int(input("Informe o angulo? "))
print("\n Cos({}) = {:.2}\n Sen({}) = {:.2f}\n Tg({}) = {:.2}" .format(angulo, math.cos(angulo), angulo, math.sin(angulo), angulo, math.tan(angulo)))
