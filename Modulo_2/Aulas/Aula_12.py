nome = str(input("Qual é o seu nome? "))
if nome == 'Wilham':
    print("{}, que nome bonito!" .format(nome))
elif nome == 'Anastácia' or nome == 'Carmela':
    print("Gostei do seu nome {}!" .format(nome))
elif nome == 'Pedro' or nome == 'João':
    print("{}, O seu nome é muito popular." .format(nome))
else:
    print("{}, o seu nome é tão normal." .format(nome))
print("Tenha um bom dia.")