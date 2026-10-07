# Проект FitLife - MVP версия 1.0

# 1. Обозначение ограничений
MIN_WEIGHT, MAX_WEIGHT = 8, 200
MIN_HEIGHT, MAX_HEIGHT = 1.2, 2.3
MIN_AGE, MAX_AGE = 5, 120
ML_PER_KG = 30        # мл воды на 1 кг веса
ML_PER_LITER = 1000   # мл в одном литре


# 2. Функция запроса
def ask_number(question, min_value, max_value, example, cast=float):
    """Спрашивает у пользователя число и проверяет, что оно в диапазоне."""
    while True:
        raw = input(question)
        raw = raw.replace(',', '.')  # чтобы "1,70" тоже сработало
        try:
            value = cast(raw)
        except ValueError:
            print(f'Нужно ввести число (например, {example}). Попробуй ещё.')
        else:
            if min_value <= value <= max_value:
                return value
            print(f'Значение должно быть от {min_value} до {max_value}.')


# 3. Знакомство
print('Привет! Я бот FitLife. Давай познакомимся.')
user_name = input('Как тебя зовут? ')

# 4. Сбор данных
user_age = ask_number(
    'Сколько тебе лет? ',
    MIN_AGE, MAX_AGE,
    example='30',
    cast=int
)
user_weight = ask_number(
    'Введи свой вес (в кг): ',
    MIN_WEIGHT, MAX_WEIGHT,
    example='75.5'
)
user_height = ask_number(
    'Введи свой рост (в метрах, например 1.70): ',
    MIN_HEIGHT,
    MAX_HEIGHT,
    example='1.70'
)

# 5. Логика расчетов
# Формула ИМТ: вес разделить на (рост в квадрате)
user_imt = round(user_weight / (user_height ** 2), 1)
water_ml = user_weight * ML_PER_KG
water_l = round(water_ml / ML_PER_LITER, 2)

# Доп расчет категории ИМТ
if user_imt < 18.5:
    category = 'недостаточный вес'
elif user_imt < 25:
    category = 'норма'
elif user_imt < 30:
    category = 'избыточный вес'
else:
    category = 'ожирение'

# 6. Вывод красивого результата
print()
print(f'Отчёт для пользователя: {user_name}, {user_age} лет')
print(f'Твой Индекс Массы Тела: {user_imt} кг/м^2 ({category})')
print(f'Рекомендуемая норма воды: {water_l} л. в день')
print()
print('Расчёт окончен. Будьте здоровы!')
