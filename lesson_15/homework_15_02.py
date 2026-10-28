import json
import logging
from pathlib import Path

# 1. Вказуємо шляхи до директорії та лог-файлу
dir_path = Path("ideas_for_test/work_with_json")
log_file_path = dir_path / "json__kovalisko.log"

# 2. Налаштовуємо логер
logger = logging.getLogger("json_validator")
logger.setLevel(logging.ERROR)

# Створюємо файловий хендлер для запису логів у файл
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")
file_handler.setLevel(logging.ERROR)

# Формат логування: дата/час - рівень - повідомлення
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

valid_files_count = 0
invalid_files_count = 0

# 3. Перевіряємо всі .json файли у теці
for file_path in dir_path.glob("*.json"):
    try:
        with open(file_path, mode="r", encoding="utf-8") as f:
            json.load(f)  # Намагаємося розпарсити файл
        valid_files_count += 1
        print(f"[OK] Файл валідний: {file_path.name}")
    except (json.JSONDecodeError, Exception) as e:
        invalid_files_count += 1
        # Логуємо помилку на рівні ERROR у лог-файл
        logger.error(f"Файл '{file_path.name}' не є валідним JSON. Помилка: {e}")
        print(f"[ERROR] Файл НЕВАЛІДНИЙ: {file_path.name}")

# 4. Підсумок у консоль
print("\n--- Результати перевірки ---")
print(f"Валідних файлів: {valid_files_count}")
print(f"Невалідних файлів: {invalid_files_count}")
print(f"Лог помилок збережено у: {log_file_path}")