print("\033[1;31;43m Olá, Mundo! \033[m")
print("\033[4;30;45m Bom dia \033[m")
print("\033[7;33;44m Byebye \033[m")

a = 3
b = 5
print("Os valores são \033[32m {} \033[m e \033[31m {} \033[m." .format(a, b))

nome = 'Wilham Mendes'
cores = {'limpa' : '\033[m',
         'azul' : '\033[34m', 
         'amarelo' : '\033[4;33m',
         'preto_e_branco' : '\033[7;30m'}

print("\nOlá, muito prazer em te conhecer, {}{}{}!!!\n" .format(cores['azul'], nome, cores['limpa']))
print("{}Tens um nome muito bonito.{}\n" .format(cores['amarelo'], cores['limpa']))