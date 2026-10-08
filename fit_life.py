# Проект FitLife - MVP версия 1.0

# 1. Обозначение ограничений
MIN_WEIGHT, MAX_WEIGHT = 8, 200
MIN_HEIGHT, MAX_HEIGHT = 1.2, 2.3
MIN_AGE, MAX_AGE = 5, 120
ML_PER_KG = 30        # мл воды на 1 кг веса
ML_PER_LITER = 1000   # мл в одном литре


# 2. Знакомство
print('Привет! Я бот FitLife. Давай познакомимся.')
user_name = input('Как тебя зовут? ')


# Диляра я сделал сначала все проверки в одном блоке
# но так не получается пройти авто проверку.
# я написал тебе письмо с перечнем ошибок
# но с почтой Я сегодня беда(
# поэтому так:
# 3. Сбор данных
# Возраст
while True:
    try:
        user_age = int(input('Сколько тебе лет? '))
    except ValueError:
        print('Ошибка: возраст должен быть целым числом.')
    else:
        if MIN_AGE <= user_age <= MAX_AGE:
            break
        print(f'Возраст должен быть от {MIN_AGE} до {MAX_AGE}.')

# Вес
while True:
    try:
        user_weight = float(input('Введи свой вес (в кг): '))
    except ValueError:
        print('Ошибка: нужно ввести число (например, 75.5).')
    else:
        if MIN_WEIGHT <= user_weight <= MAX_WEIGHT:
            break
        print(f'Вес должен быть от {MIN_WEIGHT} до {MAX_WEIGHT}.')

# Рост
while True:
    try:
        user_height = float(input('Введи свой рост (в метрах): '))
    except ValueError:
        print('Ошибка: нужно ввести число (например, 1.70).')
    else:
        if MIN_HEIGHT <= user_height <= MAX_HEIGHT:
            break
        print(f'Рост должен быть от {MIN_HEIGHT} до {MAX_HEIGHT}.')


# 4. Логика расчетов
user_imt = round(user_weight / (user_height ** 2), 1)
water_ml = user_weight * ML_PER_KG
water_l = round(water_ml / ML_PER_LITER, 2)

if user_imt < 18.5:
    category = 'недостаточный вес'
elif user_imt < 25:
    category = 'норма'
elif user_imt < 30:
    category = 'избыточный вес'
else:
    category = 'ожирение'


# 5. Вывод результата
print()
print(f'Отчёт для пользователя: {user_name}, {user_age} лет')
print(f'Твой Индекс Массы Тела: {user_imt} кг/м^2 ({category})')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print('Расчёт окончен. Будьте здоровы!')
