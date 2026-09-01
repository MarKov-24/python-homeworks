import math

# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = (
    '"Would you tell me, please, which way I ought to go from here?"\n'
    '"That depends a good deal on where you want to get to," said the Cat.\n'
    '"I don\'t much care where ——" said Alice.\n'
    '"Then it doesn\'t matter which way you go," said the Cat.\n'
    '"—— so long as I get somewhere," Alice added as an explanation.\n'
    '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
)

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
single_quotes = [char for char in alice_in_wonderland if char == "'"]
print(f"task 02: Знайдено символів одинарної лапки ('): {len(single_quotes)}")

# task 03 == Виведіть змінну alice_in_wonderland на друк
print("task 03:")
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
total_sea_area = black_sea  + azov_sea
print(f"task 04: {total_sea_area}")

# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_goods = 375291
goods_1_and_2 = 250449
goods_2_and_3 = 222950
goods_3 = total_goods - goods_1_and_2
goods_1 = total_goods - goods_2_and_3
goods_2 = goods_1_and_2 - goods_1
print(f"task 05: goods_1 = {goods_1}; goods_2 = {goods_2}; goods_3 = {goods_3}")

# task 06
"""
Михайло разом з батьками вирішили купити комп'ютер, ско-
риставшись послугою 'Оплата частинами'. Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп'ютера.
"""
months = 18
monthly_payment = 1179
laptop_cost = months * monthly_payment
print(f"task 06: {laptop_cost}")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
rem_a = 8019 % 8
rem_b = 9907 % 9
rem_c = 2789 % 5
rem_d = 7248 % 6
rem_e = 7128 % 5
rem_f = 19224 % 9
print(f"task 07 (остачу від діленя чисел): rem_a = {rem_a}; rem_b = {rem_b}; rem_c = {rem_c}; rem_d = {rem_d}; rem_e = {rem_e} ; rem_f = {rem_f}")

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_big = 4 * 274
pizza_medium = 2 * 218
juice = 4 * 35
cake = 1 * 350
water = 3 * 21
total_party_cost = pizza_big + pizza_medium + juice + cake + water
print(f"task 08 (скільки грошей знадобиться): {total_party_cost} грн")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
total_photos = 232
photos_per_page = 8
pages_needed = math.ceil(total_photos /photos_per_page)
print(f"task 09 (скількість сторінок): {pages_needed} шт")

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
consumption_per_100km = 9
tank_capacity = 48
total_fuel = (distance / 100) * consumption_per_100km
pit_stops = math.ceil(total_fuel/tank_capacity)
print(f"task 10: total_fuel = {total_fuel}; pit_stops = {pit_stops}")