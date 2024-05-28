dias = float(input('Digite a quantidade de dias: '))
percorrido = float(input('Digite a KM percorrida: '))
total = (dias * 60) + (percorrido * 0.15)
print(f'Total a pagar é: {total:.2f}')
