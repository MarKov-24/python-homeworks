def calculate_average(numbers: list[float | int]) -> float | int:
    """Обчислює середнє арифметичне списку чисел."""
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def reverse_string(text: str) -> str:
    """Повертає перевернутий рядок."""
    return text[::-1]

def find_longest_word(words: list[str]) -> str:
    """Знаходить найдовше слово у списку рядків."""
    if not words:
        return ""
    return max(words, key=len)

def even_sum(numbers: list[int]) -> int:
    """Обчислює суму лише парних чисел зі списку."""
    return sum(num for num in numbers if num % 2 == 0)

def is_unique_symbols_count_greater_10(text: str) -> bool:
    """Перевіряє, чи кількість унікальних символів у тексті більша за 10."""
    unique_symbols = set(text)
    count = len(unique_symbols)
    if count > 10:
        return True
    else:
        return False