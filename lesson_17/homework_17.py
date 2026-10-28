# ==========================================
# ЧАСТИНА 1: ГЕНЕРАТОРИ
# ==========================================

# 1. Генератор, який повертає послідовність парних чисел від 0 до N
def even_numbers_generator(n):
    for num in range(0, n + 1, 2):
        yield num


# 2. Генератор, який генерує послідовність Фібоначчі до певного числа N
def fibonacci_generator(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b


# ==========================================
# ЧАСТИНА 2: ІТЕРАТОРИ
# ==========================================

# 1. Ітератор для зворотного виведення елементів списку
class ReverseIterator:
    def __init__(self, data_list):
        self.data_list = data_list
        self.index = len(data_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index <= 0:
            raise StopIteration
        self.index -= 1
        return self.data_list[self.index]


# 2. Ітератор, який повертає всі парні числа в діапазоні від 0 до N
class EvenRangeIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration
        val = self.current
        self.current += 2
        return val


# ==========================================
# ЧАСТИНА 3: ДЕКОРАТОРИ
# ==========================================

# 1. Декоратор, який логує аргументи та результати викликаної функції
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Виклик функції '{func.__name__}' з аргументами: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Функція '{func.__name__}' повернула результат: {result}")
        return result
    return wrapper


# 2. Декоратор, який перехоплює та обробляє винятки
def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"[ПОМИЛКА] У функції '{func.__name__}' виник виняток: {e}")
            return None
    return wrapper


# ==========================================
# ПРИКЛАДИ ВИКОРИСТАННЯ (можна розкоментувати)
# ==========================================
if __name__ == "__main__":
    print("--- Тест генератора парних чисел ---")
    for n in even_numbers_generator(6):
        print(n, end=" ")
    print()

    print("\n--- Тест генератора Фібоначчі ---")
    for f in fibonacci_generator(100):
        print(f, end=" ")
    print()

    print("\n--- Тест зворотного ітератора ---")
    for item in ReverseIterator([10, 20, 30, 40]):
        print(item, end=" ")
    print()

    print("\n--- Тест ітератора парних чисел ---")
    for ev in EvenRangeIterator(8):
        print(ev, end=" ")
    print()

    print("\n--- Тест декоратора логування ---")
    @log_function
    def multiply(a, b):
        return a * b
    multiply(4, 5)

    print("\n--- Тест декоратора обробки винятків ---")
    @handle_exceptions
    def divide(a, b):
        return a / b
    divide(10, 0)