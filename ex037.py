num = int(input('Digite um numero inteiro: '))
print('''Escolha uma das bases para conversão: 
[ 1 ] - Converter para Binário
[ 2 ] - Converter para OCTAL
[ 3 ] - Converter para HEXA''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print(f'{num} convertido para Binário é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} convertido para Octal é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} convertido para Hexa é igual a {hex(num)[2:]}')
else:
    print('Opção Inválida!')
