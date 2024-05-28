import math

oposto = float(input('Cateto Oposto: '))
adjacente = float(input('Cateto Adjacente: '))
print(f'O comprimento da hipotenusa é: {math.hypot(oposto, adjacente):.2f}')