nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))

print('{2} tem {1} anos de idade e seu imc é {0:.2f}'.format(imc, idade, nome))

print('{nm} tem {id} anos de idade e seu imc é {im:.2f}'.format(im = imc, id = idade, nm = nome))
