frase = 'Curso em vídeo Python'

print(frase)

# Fatiar a frase
print("\n\nFrase fatiada:")
print(frase[5::2])

# Contar uma letra
print("\n\nLetras contadas:")
print(frase.count('o'))


# Contar o total das letras existentes numa frase
print("\n\nO total das letras existentes na frase são:")
print(len(frase))


# Colocar todas as letras em maiúscolas
print("\n\nSegue a frase modificada:")
print(frase.upper())


# Contar quantas vezes a letra "O" apareceu na frase  modificada
print("\n\nA letra 'O' apareceu:")
print(frase.upper().count('O'))

# Remover os espaços a esquesda e a direita da frase
fras = '      Curso em vídeo Python      '

print("\n\nQuantidade de pequenos espaços e letras contidas na fras:")
print(len(fras))

print("\n\nQuantidade de pequenos espaços, sendo que os espaços antes e depois da frase foram eliminados:")
print(len(fras.strip()))


# Replace, isto é, subtituir, porém temporariamente
print('\n\nReplace, isto é, subtituir, porém temporariamente.\nObs. a diferença')
print(frase.replace('Python', 'Android'))
print(frase)


# Replace, isto é, subtituir definitivamente
print('\n\nReplace, isto é, subtituir definitivamente')
frase = frase.replace('Python', 'Android')
print(frase)
print(frase, '\n\n')


# Verifica se existe uma palavra numa frase
print('Android' in frase)


# Ache uma palavra numa frase
print(frase.find('em'))
print(frase.lower().find('android'))


# Separar uma frase
print('\n\n')
print(frase.split())
dividido = frase.split()
print("\n\nImprime 2ª letra da 3ª palavra")
print(dividido[2] [1])