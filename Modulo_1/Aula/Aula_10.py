"""
nome = str(input("Qual é o seu nome? "))
print("Bom dia, prazer en te conhecer {}!" .format(nome))
if nome == 'Wilham':
    print("{}, que nome lindo você tem!" .format(nome))
else:
    print("{}, o seu nome é muito vulgar." .format(nome))
"""


n1 = float(input("Informe a 1ª nota: "))
n2 = float(input("Informe a 2ª nota: "))
media = (n1 + n2)/2
print("A sua média é de: {}" .format(media))
if media >= 4 and media <= 7:
    print("Você tem que fazer AF. Boa sorte.")
elif media >= 7:
    print("Parabéns, você aprovou!")
else:
    print("Você reprovou, estude mais no proximo semestre.")

