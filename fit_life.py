# Проект FitLife - MVP версия 1.0

# 1. Знакомство
print('Привет! Я бот FitLife. Давай познакомимся.')
user_name = input('Как тебя зовут? ')
user_age = int(input('Сколько тебе лет? '))


# 2. Сбор данных
# 2.1 Jбозначение ограничений
min_weight = 8
max_weight = 200
min_height = 1
max_height = 2.3
while True:
    try:
        user_weight = float(input('Введи свой вес (в кг): '))
    except ValueError:
        print('Нужно ввести число (например, 75.5). Попробуй еще раз.')
    else:
        if user_weight < min_weight or user_weight > max_weight:
            print(f'Вес должен быть от {min_weight} до {max_weight} кг.')
            print('Попробуйте снова.')
            continue
        break        
while True:
    try:
        user_height = input('Введи свой рост (в метрах, например 1.70): ')
        user_height = float(user_height)
    except ValueError:
        print('Введи рост через точку, например 1.70')
        print('Другие символы не подходят')
    else:
        if user_height < min_height or user_height > max_height:
            print(f'Рост должен быть от {min_height} до {max_height} метров.')
            print('Попробуйте снова.')
            continue
        break

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
