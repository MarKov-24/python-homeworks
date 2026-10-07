import pytest

from homeworks import (
    calculate_average,
    even_sum,
    find_longest_word,
    is_unique_symbols_count_greater_10,
    reverse_string,
)

# Тести для функції calculate_average

def test_calculate_average_positive():
    """Позитивний тест: коректний розрахунок для списку чисел."""
    assert calculate_average([10, 20, 30, 40]) == 25.0

def test_calculate_average_empty():
    """Граничний випадок: порожній список повертає 0."""
    assert calculate_average([]) == 0

def test_calculate_average_negative_numbers():
    """Позитивний тест: список з від'ємними числами."""
    assert calculate_average([-10, 10, -5, 5]) == 0.0

def test_calculate_average_invalid_type():
    """Негативний тест: передача рядка замість списку чисел викликає TypeError."""
    with pytest.raises(TypeError):
        calculate_average("not_a_list")

def test_calculate_average_with_string_inside():
    """Негативний тест: елементи списку мають некоректний тип даних (рядок замість числа)."""
    with pytest.raises(TypeError):
        calculate_average([10, "20", 30])

# Тести для функції reverse_string

def test_reverse_string_positive():
    """Позитивний тест: перевертання звичайного рядка."""
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_empty():
    """Граничний випадок: порожній рядок."""
    assert reverse_string("") == ""

# Тести для функції find_longest_word

def test_find_longest_word_positive():
    """Позитивний тест: пошук найдовшого слова зі списку."""
    words = ["cat", "elephant", "dog", "hippopotamus"]
    assert find_longest_word(words) == "hippopotamus"

def test_find_longest_word_empty():
    """Граничний випадок: порожній список повертає порожній рядок."""
    assert find_longest_word([]) == ""

# Тести для функції even_sum

def test_even_sum_positive():
    """Позитивний тест: підрахунок суми лише парних чисел."""
    assert even_sum([1, 2, 3, 4, 5, 6]) == 12

def test_even_sum_no_even_numbers():
    """Граничний випадок: якщо парних чисел немає, повертається 0."""
    assert even_sum([1, 3, 5, 7]) == 0

# Тести для функції is_unique_symbols_count_greater_10

def test_is_unique_symbols_count_greater_10_true():
    """Позитивний тест: більше 10 унікальних символів (повертає True)."""
    # 11 унікальних символів: abcdefghijk
    assert is_unique_symbols_count_greater_10("abcdefghijk") is True

def test_is_unique_symbols_count_greater_10_false():
    """Негативний тест: менше або дорівнює 10 унікальних символів (повертає False)."""
    # 10 унікальних символів: abcdefghij
    assert is_unique_symbols_count_greater_10("abcdefghij") is False

def test_is_unique_symbols_count_greater_10_repeating_chars():
    """Граничний випадок: довгий рядок, але унікальних символів менше 10."""
    assert is_unique_symbols_count_greater_10("aaaaaaaaaaaaaaa") is False