try:
    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))

    if x == 0 and y == 0:
        print("Точка находится в начале координат.")
    elif x == 0:
        print("Точка лежит на оси Y.")
    elif y == 0:
        print("Точка лежит на оси X.")
    elif x > 0 and y > 0:
        print("Точка в I четверти.")
    elif x < 0 and y > 0:
        print("Точка во II четверти.")
    elif x < 0 and y < 0:
        print("Точка в III четверти.")
    elif x > 0 and y < 0:
        print("Точка в IV четверти.")
except ValueError:
    print("Ошибка: введите корректные числа!")