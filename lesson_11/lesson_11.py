def sum_numbers_in_string(text):
    # Розбиваємо рядок за комами на окремі елементи
    items = text.split(",")
    total = 0

    try:
        # Перетворюємо кожен елемент на число та додаємо до суми
        for item in items:
            total += int(item)
        return total
    except ValueError:
        # Якщо некоректні текст або число — повертаємо повідомлення
        return "Не можу це зробити!"

# Створюємо масив (список) зі строками
data_list = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

# Виводимо результат
for item in data_list:
    result = sum_numbers_in_string(item)
    print(result)