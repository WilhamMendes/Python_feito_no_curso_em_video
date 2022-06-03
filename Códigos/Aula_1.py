from winreg import QueryInfoKey


print('\nOlá, mundo!')

print(7+3)

print('7' + '4')

print('\nNúmero: ', 5)

nome = 'Wilham'
idade = 20
peso = 72

print(nome, 'tem', idade, 'anos', 'e pesa', peso, '\n\n')

# ITERATIVIDADE

nome_1 = input('Qual é o seu nome? ')
idade_1 = input('Qual é a sua idade? ')
peso_1 = input('Qual é o seu peso? ')

print('\nNome:', nome_1, 'Idade:', idade_1, 'Peso:', peso_1)

# Desafio 

nom = input('\nQual é o seu nome? ')
print('Olá', nom, '.', 'Prazer em te conhecer!\n')

ano_nas = input('\nEm que ano você nasceu? ')
mes = input('Em que mês você nasceu? ')
dia = input('Em que dia você nasceu? ')

print('\n\n')
print(nom, ', você nasceu no dia', dia, 'de', mes, 'do ano', ano_nas, '. Correto?')
