#task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    multiplier = 1
    while True :
        result = number * multiplier
        if  result > 25:
           break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
print("task 1")
multiplication_table(3)

#task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def sum_two_numbers(a, b):
    return a + b
print(f"task 2 (суму двох чисел): {sum_two_numbers(5, 10)}")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)
print(f"task 3 (середнє арифметичне списку чисел): {calculate_average([0, 20, 30, 40])}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def reverse_string(text):
    return text[::-1]
text = "Python"
print(f"task 4 (рядок у зворотному порядку) '{text}': {reverse_string(text)}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def find_longest_word(words):
    if not words:
        return ""
    return max(words, key=len)
words_list = ["Доба", "Ніч", "Ранок"]
print(f"task 5 (найдовше слово): {find_longest_word(words_list)}")

 # task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""

def find_substring(str1, str2):
    return str1.find(str2)
str1 = "Добрий вечір!"
str2 = "вечір"
print(f"task 6 (Індекс першого входження): {find_substring(str1, str2)}")
str1 = "Вечірній Львів"
str2 = "лев"
print(f"task 6 (Індекс першого входження): {find_substring(str1, str2)}")

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""

# task 7 знайти унікальні символи
def is_unique_symbols_count_grater_10(text):
    unique_symbols = set(text)
    count = len(unique_symbols)
    if count > 10:
        return True
    else:
        return False
text = "qwertyuiopasd"
print(f"task 7 (знайти унікальні символи) > 10: '{text}': {is_unique_symbols_count_grater_10(text)}")
text = "qwerty"
print(f"task 7 (знайти унікальні символи) > 10: '{text}': {is_unique_symbols_count_grater_10(text)}")

# task 8 сформувати новий список, який містить лише змінні типу стрінг
def filter_strings(lst):
    result = []
    for item in lst:
        if isinstance(item, str):
            result.append(item)
    return result
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = filter_strings(lst1)
print(f"task 8 (новий список, який містить лише змінні типу стрінг): {lst2})")

# task 9 порахувати суму усіх парних чисел
def even_sum(numbers):
    return sum(num for num in numbers if num % 2 == 0)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("task 9 (cума парних чисел):", even_sum(numbers))

# task 10 обчислити яку площу займають Чорне та Азовське моря разом
def calculate_total_sea_area(sea1_area, sea2_area):
    return sea1_area + sea2_area
black_sea = 436402
azov_sea = 37800
total_sea_area = calculate_total_sea_area(black_sea, azov_sea)
print(f"task 10 (площа морів): {total_sea_area}")