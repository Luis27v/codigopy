lados = input().split()

A, B, C = sorted(map(float, lados),revere=True)
if A >= (B + C):
   print('nao forma triangulo')
else: 
    if (A*A) == (B * B + C*C):
        print ('triangulo retangulo')
    elif (A * A) > ((B*B + C * C)):
        print ('triangulo obtusangulo')
    elif (A *A) < ((B * B) + (C *C)):
        print ('triangulo ')
