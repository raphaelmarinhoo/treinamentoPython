ladoA = float(input('Lado A: '))
ladoB = float(input('Lado B: '))
ladoC = float(input('Lado C: '))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print('É um triangulo!')
else:
    print('Não é um triangulo.')