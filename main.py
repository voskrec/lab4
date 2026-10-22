import math
#вводим числа
a=int(input('введите a:'))
b=int(input('введите b:'))
c=int(input('введите c:'))
#высчитываем дескриминант
if a==0:
    print('не квадратное')
else:
    D=b**2-4*a*c
    if D>0:
        x1=(-b+math.sqrt(D))/(2*a)
        x1=(-b-math.sqrt(D))/(2*a)
        print(f"корни x1:{x1:.2f} x2:{x2:.2f}")
    elif D==0:
        x1=-b/(2*a)
        print(f"один корень x1:{x1:.2f}")
    else:
        print('нет корней')
