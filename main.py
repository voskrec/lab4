def converter():
    while True:
        try:
            num = int(input("Введите целое положительное число в десятичной системе: "))
            if num < 0:
                print("Ошибка: число должно быть положительным!")
                continue
            break
        except ValueError:
            print("Ошибка: введите корректное целое число!")

    print(f"Десятичная: {num}")
    print(f"Двоичная: {bin(num)[2:]}")          # срез [2:] убирает префикс '0b'
    print(f"Восьмеричная: {oct(num)[2:]}")      # убирает '0o'
    print(f"Шестнадцатеричная: {hex(num)[2:].upper()}")  # убирает '0x', делает заглавные

converter()