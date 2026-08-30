# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples* 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetery = (storona_1 + storona_2 + storona_3 + storona_4)
print(f"Периметр фігури:{perimetery}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples_trees = 4
pears = apples_trees - 5
plums = apples_trees - 2
total_trees = apples_trees + pears +plums
print(f"4 + 9 + 2 = 15")

# task 08
"""
До обіда температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?

temp_morning = 5
temp_afternoon = temp_morning - 10
temp_evening = temp_afternoon + 4

temp_morning = 5 temp_afternoon = temp_morning - 10 = -5
temp_evening = -5+ 4 = -1

"""

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скількі сьогодні дітей у театральному гуртку?
"""
boys_total = 24
girls_total = boys_total / 2
boys_present = boys_total - 1
girls_present = girls_total - 10
children_present = boys_present + girls_present
print(f"boys_total = 23 хлопчиків, girl_total = 10, children_present = 33")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?

book1 = 8
book2 = book1 + 2 uhy
book3 = (book1 + book2)/2
total_price = book1 + book2 +book3
print(f"book1 = 8, book2 = book1 + 2 = 10, book3 = (8+10)/2 = 9))
"""
