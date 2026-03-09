codigo1, quantidade1, valor1 = map(float, input(). split())
codigo2, quantidade2, valor2 = map(float, input(). split())

custo1 = quantidade1 * valor1
custo2 = quantidade2 * valor2

print(f'VALOR A PAGAR: R$ {(custo1 + custo2): .2f}')