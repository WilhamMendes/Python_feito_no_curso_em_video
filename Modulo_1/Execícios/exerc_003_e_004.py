a = input("Digite algo: ")

print("\nO tipo primitivo desse valor é: ", type(a))
print("Só tem espaço: ", a.isspace()) # isspace é um método
print("É um número? ", a.isnumeric())
print("É alpha numerico? ", a.isalnum())
print("Está em maiúsculas? ", a.isupper())
print("Esrá em minúsculas? ", a.islower())
print("Está capitalizada? ", a.istitle()) 