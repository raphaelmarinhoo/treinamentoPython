import random

a = input('Primeiro nome: ')
b = input('Segundo nome: ')
c = input('Terceiro nome: ')
d = input('Quanto nome: ')
ordem = [a, b, c, d]
random.shuffle(ordem)
print(f'O vencedor é {ordem}')

