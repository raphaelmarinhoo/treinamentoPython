from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento: '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar imediatamente!')
elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento.')
else:
    saldo = idade - 18
    print(f'Você deveria ter se alistado há {saldo} anos.')
