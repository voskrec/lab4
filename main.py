try:
    weight = float(input("Введите ваш вес (кг): "))
    height = float(input("Введите ваш рост (м, например 1.75): "))

    if weight <= 0 or height <= 0:
        print("Ошибка: вес и рост должны быть положительными числами!")
    else:
        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Недостаточный вес"
        elif bmi < 25:
            category = "Норма"
        elif bmi < 30:
            category = "Избыточный вес"
        else:
            category = "Ожирение"

        print(f"Ваш ИМТ: {bmi:.2f}")
        print(f"Категория: {category}")
except ValueError:
    print("Ошибка: введите корректные числовые значения!")