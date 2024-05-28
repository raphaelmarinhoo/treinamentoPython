ladoA = float(input('Lado A: '))
ladoB = float(input('Lado B: '))
ladoC = float(input('Lado C: '))

if ladoA < ladoB + ladoC and ladoB < ladoA + ladoC and ladoC < ladoA + ladoB:
    print('É um triangulo! ', end='')
    if ladoA == ladoB == ladoC:
        print('EQUILATERO!')
    elif ladoA != ladoB != ladoC != ladoA:
        print('ESCALENO!')
    else:
        print('ISOCELES!')
else:
    print('Não é um triangulo.')
