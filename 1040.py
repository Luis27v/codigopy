n1, n2, n3, n4 = map(float, (input()). split (' '))

media = (n1*2 + n2 * 3 + n3 * 4 + n4 * 1 )/ (2 + 3 + 4 + 1)
print(f'Media: {media: .1f}')

if media >= 7:
    print('aluno aprovado.')
elif media >= 5:
    print('aluno em exame')
elif media <= 3:
    print('aluno reprovado')

n5 = float(input())
print("nota de exame: {:1.f}".format(n5))
media = (media + n5) / 2

if media >= 5:
    print ('aluno aprovado.')
else:
    print ('aluno reprovado.')
                                    