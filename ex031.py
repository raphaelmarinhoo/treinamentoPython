km = int(input('Qual a distância da viagem? '))
if km <= 200:
    print(f'O valor da viagem é: R${km * 0.50:.2f}')
else:
    print(f'O valor da viagem é: R${km * 0.45:.2f}')
