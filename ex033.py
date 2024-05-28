num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = int(input('Terceiro número: '))
if num1 > num2 and num1 > num3:
    print('Primeiro número é maior.')
elif num2 > num1 and num2 > num3:
    print('Segundo número é maior.')
else:
    print('Terceiro número é maior')
