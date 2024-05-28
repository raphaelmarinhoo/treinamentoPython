salario = float(input('Digite o salario: '))
if salario >= 1250:
    print(f'Salário com aumento: {salario + ((salario * 10) / 100):.2f}')
else:
    print(f'Salário com aumento: {salario + ((salario * 15) / 100):.2f}')
