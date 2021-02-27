# > - Esquerda
# < - Direita
# ^ - Centro

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print(f'{divisao:.2f}')

nome = 'Hebert'
print(f'{nome:#^16}')

num_1 = 1234
print(f'{num_1:0>10}')

print(f'{num_1:0>10.2f}')

nome = 'Hebert'
sobrenome = 'Falcão'
nome_formatado = '{0:$^50}{1:#>50}'.format(nome, sobrenome)
print(nome_formatado)


nome = 'hebert falcão'
print(nome.lower())
print(nome.upper())
print(nome.title())