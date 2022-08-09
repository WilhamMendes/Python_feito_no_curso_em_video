
"""
# Exercício 036
print("***"*20)
print("Benvindo/a ao emprestimos bancario")
print("***"*20)

valor_casa = float(input("Qual é o preço da casa? "))
salario = float(input("Qual é o seu salário? "))
parcelas = int(input("Em quantas parcelas pretendes pagar a casa? "))

quantia_por_mes = valor_casa / parcelas

if quantia_por_mes > (salario * 0.3):
    print("Infelizmente não podemos realizar o emprestimo.")
else:
    print("Parabéns, você conseguiu o emprestimo.")
"""



# Exercício 037
print("***"*20)
print("Escreva um número inteiro qualquer para converter em binário, octal ou hexadecimal")
print("***"*20)

num = int(input("Qual é o número que queres converter? "))
opcoes = int("DIGITE:\n1 Para converter em BNÁRIO\n2 Para converter em OCTAL\n3 Para converter em HEXADECIMAL")


