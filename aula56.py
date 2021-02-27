import copy

#### Exemplo 01
d1 = {'chave1': 'valor1', 'chave2': 'valor2'}
print(d1)

d1['chave3'] = 'valor3'
print(d1)

print(d1['chave1'])

#### Exemplo 02
d1 = dict(chave1 = 'valor1', chave2 = 'valor2')
print(d1)

#### Exemplo 03
d1 = dict(chave1 = 'valor1', chave2 = 'valor2')
print(d1)

d1['chave3'] = 'valor3'
print(d1)

d1['chave3'] = 'valor33333'
print(d1)

#### Exemplo 04
d1 = {
    'str': 'valor str',
    123: 'valor 123',
    (1, 2, 3, 4): 'Tupla'
}

print(d1[(1, 2, 3, 4)])

#### Exemplo 05
d1 = dict(chave1 = 'valor1', chave2 = 'valor2')

if 'chave4' in d1:
    print('existe chave4')
else:
    print('não existe chave4')

if 'chave1' in d1:
    print('existe chave1')
else:
    print('não existe chave1')

print('chave1', d1.get('chave1'))

#### Exemplo 06
d1 = dict(chave1 = 'valor1', chave2 = 'valor2')

if d1.get('chave1') is not None:
    print(d1.get('chave1'))

#### Exemplo 07
d1 = dict(chave1 = 'valor1', chave2 = 'valor2', chave3 = 'valor3')

del d1['chave1']
print(d1)

#### Exemplo 08
d1 = dict(chave1 = 'valor1', chave2 = 'valor2', chave3 = 'valor3')

print(d1.keys())
print(d1.values())
print(d1.items())

#### Exemplo 09
clientes ={
    'cliente1': {
        'nome': 'Luiz',
        'sobrenome': 'Otávio',
    },
    'cliente2': {
        'nome': 'João',
        'sobrenome': 'Moreira',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'clientes_k: {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'dados_k: {dados_k} - dados_v: {dados_v}')

#### Exemplo 10
d1 = dict(chave1 = 'valor1', chave2 = 'valor2', chave3 = 'valor3', chave4 = ['João', 'Maria'])
d2 = copy.deepcopy(d1)
d3 = d1.copy()

d2['chave1'] = 'valor11111'
d2['chave4'][0] = 'Hugo'

d3['chave4'][0] = 'Hugo 2222'

print(id(d1), d1)
print(id(d2), d2)
print(id(d3), d3)