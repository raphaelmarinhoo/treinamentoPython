import math

peso = float(input('Digite o seu peso: (kg) '))
altura = float(input('Digite sua altura: (m) '))
imc = peso / math.pow(altura, 2)
print(f'O IMC dessa pessoa é de {imc:.2f}')
if imc < 18.5:
    print('Você está abaixo do peso normal.')
elif 18.5 <= imc < 25:
    print('Parabéns, você está na faixa de peso normal.')
elif 25 <= imc < 30:
    print('Você está em sobrepeso.')
elif 30 <= imc < 40:
    print('Cuidado! Você está em obesidade.')
elif imc >= 40:
    print('Cuidado! Você está em obesidade mórbida')
