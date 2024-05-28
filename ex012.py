preco = float(input('Digite o preço: '))
desconto = preco - (preco * 5) / 100
print(f'O novo preço é: {desconto:,.2F}')