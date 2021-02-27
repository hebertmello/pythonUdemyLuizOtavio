### List  Comprehension

#### Exemplo 01
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]

print(id(l1), l1)
print(id(l2), l2)

#### Exemplo 02
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [v * 2 for v in l1]

print(l2)

#### Exemplo 02
l1 = [1, 2, 3, 4]
l2 = [(v, v2) for v in l1 for v2 in range(3)]

print(l2)

#### Exemplo 03
l1 = ['Luiz', 'Mauro', 'Maria']
l2 = [v.replace('a', '@') for v in l1]

print(l2)

#### Exemplo 04
tupla = (
    ('chave1', 'valor1'),
    ('chave2', 'valor2')
)

tupla2 = [(y, x) for x, y in tupla]
print(tupla2)

#### Exemplo 05
l3 = list(range(20))

l4 = [v for v in l3 if v % 2 == 0]
print(l4)