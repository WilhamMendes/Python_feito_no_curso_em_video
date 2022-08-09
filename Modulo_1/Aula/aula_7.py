nome = str(input("\nQual é o seu nome? "))
print("\nPrazer  em te conhecer {:=^20}!\n" .format(nome))

# O comando end='' coloca dois print na mesma linha
print("Vamos Programar",  end=' ')
print("em Python")

# Operações aritmeticas

n1 = int(input("\nEntre com o primeiro valor inteiro: "))
n2 = int(input("Entre com o segundo valor inteiro: "))

soma = n1 + n2

sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
div_int = n1 // n2
rest_div = n1 % n2

print("\n A soma = {}\n A difrença = {}\n A multiplicação = {}\n A divisão = {:.3f}" .format(soma, sub, mult, div))
print(" A potência = {}\n A divisão inteira = {}\n O resto da divisão = {}" .format(pot, div_int, rest_div))
