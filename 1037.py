valor = float(input())

if 100 < valor:
    print('fora do intervalo')
elif 75 < valor:
    print ('intervalo (75,100]')
elif 50 < valor:
    print ('intervalo (50,75]')
elif 25 < valor:
    print ('intervalo (25,50]')
elif 0 <= valor:
    print('intervalo[0,25]')
    
