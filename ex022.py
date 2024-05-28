nome = input('Digite seu nome completo: ')
primeiro = nome.split()
print(f'Maiúsculo: {nome.upper()}')
print(f'Minúsculo: {nome.lower()}')
print(f'Contagem: {len(nome.strip())}')
print(f'Primeiro Nome: {len(primeiro[0])}')

