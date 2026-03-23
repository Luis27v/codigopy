x, y = map(float, input(). split())

if x == 0 and y == 0:
    print('origem')
elif x == 0:
    print ('eixo y')
elif y == 0:
    print ('eixo x')
elif x > 0 and y > 0:
    print ('q1')
elif x > 0 and y < 0:
    print ('q4')
elif x < 0 and y > 0:
    print ('q2')
elif x < 0 and y < 0:
    print ('q3')