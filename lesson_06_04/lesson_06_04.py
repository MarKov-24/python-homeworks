numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Сума парних чисел:", even_sum)
