A, B, C, = map(float, input(). split())
pi = 3.141591

Triangulo = A * C/2
Circulo = C**2 *pi
Trapezio = (A+B) *C /2
Quadrado = B**2
Retangulo = A * B

print (f'triangulo: {Triangulo: .3f}')
print (f'Circulo: {Circulo: .3f}')
print (f'Trapezio: {Trapezio: .3f}')
print (f'Quadrado: {Quadrado: .3f}')
print (f'Retangulo: {Retangulo: .3f}')
