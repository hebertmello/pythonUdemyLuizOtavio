#### Exemplo 01
tupla1 = (1, 2, 3, 'a', 'Luiz Otavio')
print(tupla1)

#### Exemplo 02
tupla2 = 1, 2, 3, 'a', 'Luiz Otavio'
print(tupla2)

#### Exemplo 03
tupla1 = 1, 2, 3, 4, 5, 6
tupla2 = 4, 5, 6, 7, 8, 9
tupla3 = tupla1 + tupla2
print(tupla3)

#### Exemplo 04
n1, n2, n3, *resto, ultimo = tupla3
print(n1)
print(n2)
print(n3)
print(resto)
print(ultimo)

#### Exemplo 05
tupla1 = (1, 2, 3) * 4
print(tupla1)

#### Exemplo 06
tupla1 = (1, 2, 3, 4, 5, 6)
tupla1 = list(tupla1)
tupla1[1] = 234
print(tupla1, type(tupla1))

tupla1 = tuple(tupla1)
print(tupla1, type(tupla1))