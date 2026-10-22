import random

s= random.randint(1, 100)

print("Я загадал число от 1 до 100.")

while True:
    try:
        a= int(input("Твой вариант: "))

        if a<s:
            print("Загаданное число больше.")
        elif a>s:
            print("Загаданное число меньше.")
        else:
            print(f"Поздравляю! Ты угадал число")
            break
    except ValueError:
        print("Ошибка: введите целое число!")