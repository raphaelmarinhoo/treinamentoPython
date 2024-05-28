n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
media = (n1 + n2) / 2
print(f'Tirando {n1:.1f} e {n2:.1f}, a média do aluno é {media:.1f}')
if 7 > media <=5:
    print('O aluno está de recuperação.')
if media < 5:
    print('Aluno Reprovado.')
else:
    print('Aluno Aprovado!')