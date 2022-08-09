


"""
# Exercício 028
from random import randint
from time import sleep

print("\n")
print("*" *20)
print("Olá, vamos fazer um joginho. \nVou pensar em um número entre 0 e 5. Tente advinhar...")
print("*" *20)

digite = int(input("\nDigite um número inteiro de 0 a 5: "))
print("Processando...\n")

sleep(2)
num_escolhido = randint(0, 5)

if digite == num_escolhido:
    print("PARABÉNS, Você venceu.")
else:
    print("Infelizmente você perdeu.\nO número escolhido pelo computador é: {} e você escolheu {}" .format(num_escolhido, digite))
print("\n")
"""


"""
# Exercício 029
veloc = float(input("\n\nInforme a velocidade do carro: "))
if veloc > 80:
    print("Você foi multado, pois o limite da velocidade estipulado é 80km/h.")
    multa = (veloc - 80) * 7
    print("A sua multa é de {:.2f} reais.\n" .format(multa))
print("Tenha um bom dia, dirija com segurança.")
"""


"""
# Exercício 030
num = int(input("Digite um numero inteiro para verificar se é par ou não: "))
if (num % 2) == 0:
    print("O número {} é par!" .format(num))
else:
    print("O número {} é ímpar!" .format(num))
print("\n")
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
from datetime import date

ano = int(input("\nQue anor quer analisar? Ci=oloque 0 para analisar o ano atula: "))

if ano == 0:
    ano = date.today().year
    
if (ano % 4) == 0 and (ano % 100) != 0 or (ano % 400) == 0:
    print("O ano {} é bissexto, pois é divisível por quatro.\n" .format(ano))
else:
    print("O ano {} NÂO é bissexto.\n" .format(ano))
"""
    


# Exercício 033
print("\n\n")
n1 = int(input("Digite o 1º valor: "))
n2 = int(input("Digite o 2º valor: "))
n3 = int(input("Digite o 3º valor: "))

print("\n\nVerificando qual é o maior entre {}, {} e {}." .format(n1, n2, n3))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
elif n3 > n1 and n3 > n2:
    maior = n3
print("O maior número é {}" .format(maior))

print("\nVerificando qual é o menor entre {}, {} e {}." .format(n1, n2, n3))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
elif n3 < n1 and n3 < n2:
    menor = n3
print("O menor número é {}" .format(menor))
print("\n\n")



"""
# Exercício 034
salario = float(input("\nQual é o seu salário? "))
print("Calculando o seu aumento:")

if salario > 1250:
    salario_aumentado = salario + ((salario * 10)/100)
    print("O seu salário era {:.2f} reais, você recebeu aumento de 10%, logo o seu novo salário é {:.2f} reais.\n" .format(salario, salario_aumentado))
else:
    salario_aumentado = salario + ((salario * 15)/100)
    print("O seu salário era {:.2f} reais, você recebeu aumento de 15%, logo o seu novo salário é {:.2f} reais.\n" .format(salario, salario_aumentado))
"""

"""
# Exercício 035
r1 = float(input("Infrome a mediada da reta 1: "))
r2 = float(input("Infrome a mediada da reta 2: "))
r3 = float(input("Infrome a mediada da reta 3: "))

print("\nVerificando se as três reetas podem formar triângulo:")
if r1 < r3 and r2 < r3 and (r1 + r2) > r3:
        print("As três reetas podem formar triângulo.")

elif r1 < r2 and r3 < r2 and (r1 + r3) > r2:
        print("As três retas podem formar triângulo.")

elif r2 < r1 and r3 < r1 and (r2 + r3) > r1:
        print("As três retas podem formar triângulo.")
else:
    print("As três retas NÂO podem formar triângulo.") 
print("\n\n")
"""