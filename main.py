#воодим числа
a=int(input("введите первое число"))
b=int(input("введите второе число"))
c=int(input("введите третье число"))
#находим максимальное
if a>b and a>c:
    max=a
elif b>a and b>c:
    max=b
else:
    max=c
print(max)
