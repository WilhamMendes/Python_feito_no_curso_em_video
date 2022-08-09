"""
# Importar biblioteca

#import math
from math import sqrt
num = int(input("\nDigite um valor: "))

#raiz = math.sqrt(num)
raiz = sqrt(num)

print("A raiz quadrada do número {} é {:.2f}" .format(num, raiz))
"""


# Randomizar um número inteiro
import random
num = random.randint(1, 10)
print("\nO número randomizado é {}\n\n" .format(num))


# Utilizando emoji
import emoji
print(emoji.emojize("\n\nOlá mundo :earth_americas: \n\n\n", use_aliases=True))