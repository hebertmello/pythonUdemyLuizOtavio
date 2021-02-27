#### Exemplo 01
s1 = {1, 2, 3, 4, 5}

print(s1)

s1.add(2)
s1.add(6)
print(s1)

s1.discard(6)
print(s1)

#### Exemplo 02
l1 = [1, 2, 1, 1, 3, 4, 5, 6, 7, 7, 7, 8]
print(l1)

l1 = set(l1)
print(l1)

#### Exemplo 03
s1 = {1, 2, 3, 4, 5, 8}
s2 = {1, 2, 3, 4, 5, 6, 7}

s3 = s1 | s2
print(s3)

s3 = s2 - s1
print(s3)

s3 = s2 ^ s1
print(s3)