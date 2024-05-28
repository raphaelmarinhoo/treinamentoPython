import random
from time import sleep

num1 = random.randrange(0, 5)
num2 = int(input('Digite um número entre 0 e 5: '))
print('Processando...')
sleep(2)
if num2 == num1:
    print('Você acertou!')
else:
    print('Você errou!')
