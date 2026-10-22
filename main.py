#вводим числа и операцию
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
operation = input("Введите операцию (+, -, *, /): ").strip()
#производим операцию над числами
match operation:
    case "+":
        print(f"Результат: {a + b}")
    case "-":
        print(f"Результат: {a - b}")
    case "*":
        print(f"Результат: {a * b}")
    case "/":
        if b == 0:
            print("Ошибка: деление на ноль!")
        else:
            print(f"Результат: {a / b:.2f}")
    case _:
        print("неккоретно")
