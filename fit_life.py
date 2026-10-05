# Проект FitLife - MVP версия 1.0

# 1. Знакомство
print('Привет! Я бот FitLife. Давай познакомимся.')
user_name = input('Как тебя зовут? ')
user_age = int(input('Сколько тебе лет? '))


# 2. Сбор данных
while True:
    try:
        user_weight = float(input('Введи свой вес (в кг): '))
        if user_weight < 8 or user_weight > 200:
            print('Ошибка: вес должен быть от 8 до 200 кг. Попробуйте снова.')
            continue
        break
    except ValueError:
        print('Ошибка: нужно ввести число (например, 75.5). Попробуй еще раз.')
while True:
    try:
        user_height = input('Введи свой рост (в метрах, например 1.70): ')
        user_height = float(user_height)
        if user_height < 1.0 or user_height > 2.5:
            print('Рост должен быть от 1.0 до 2.5 метров. Попробуйте снова.')
            continue
        break
    except ValueError:
        print('Введи рост через точку, например 1.70')
        print('Другие символы не подходят')

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
user_imt = round(user_weight / (user_height ** 2), 1)


# Подсчет воды: вес * 30 мл
water_ml = user_weight * 30
water_l = round(water_ml / 1000, 2)


# 4. Вывод красивого результата
print()
print(f'Отчёт для пользователя: {user_name}, {user_age} лет')
print(f'Твой Индекс Массы Тела: {user_imt} кг/м^2')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print('Расчёт окончен. Будьте здоровы! ')
