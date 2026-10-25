import csv
from pathlib import Path

# Шлях до теки з файлами та файлу результату
dir_path = Path("ideas_for_test/work_with_csv")
output_path = dir_path / "result_kovalisko.csv"

# Запитуємо користувача в консолі про режим перевірки дублікатів
print("Виберіть режим видалення дублікатів:")
print("1 - Порівнювати всі колонки повністю")
print("2 - Порівнювати лише за ContactID та EmailAddress")
choice = input("Введіть 1 або 2: ").strip()

unique_rows = set()
seen_identifiers = []  # Для відстеження унікальних ID/Email при другому режимі
header = None
total_rows_read = 0

# Проходимо циклом по всіх CSV-файлах у теці
for file_path in dir_path.glob("*.csv"):
    if file_path.name.startswith("result_"):
        continue

    with open(file_path, mode="r", encoding="utf-8") as f:
        reader = csv.reader(f)
        file_header = next(reader, None)

        if header is None and file_header:
            header = [col.strip() for col in file_header]

        for row in reader:
            if row:
                total_rows_read += 1
                cleaned_row = [cell.strip() for cell in row]

                if choice == "2" and header:
                    # Режим 2: шукаємо індекси колонок ContactID та EmailAddress
                    try:
                        id_idx = header.index("ContactID")
                        email_idx = header.index("EmailAddress")

                        # Формуємо ключ для перевірки з унікальних полів
                        contact_id = cleaned_row[id_idx] if id_idx < len(cleaned_row) else ""
                        email = cleaned_row[email_idx] if email_idx < len(cleaned_row) else ""
                        identifier = (contact_id, email)

                        # Якщо такий ContactID або Email ще не зустрічалися — додаємо рядок
                        if identifier not in seen_identifiers:
                            seen_identifiers.append(identifier)
                            unique_rows.add(tuple(cleaned_row))
                    except ValueError:
                        # Якщо колонок раптом немає, падаємо на звичайне додавання рядка
                        unique_rows.add(tuple(cleaned_row))
                else:
                    # Режим 1: порівнюємо рядок повністю
                    unique_rows.add(tuple(cleaned_row))

# Рахуємо кількість видалених дублікатів
duplicates_count = total_rows_read - len(unique_rows)

# Записуємо заголовок та унікальні рядки у новий файл
with open(output_path, mode="w", encoding="utf-8", newline="") as out_file:
    writer = csv.writer(out_file)
    if header:
        writer.writerow(header)
    writer.writerows(unique_rows)

print(f"\nГотово! Результат збережено у: {output_path}")
print(f"Опрацьовано рядків (без заголовків): {total_rows_read}")
print(f"Кількість унікальних рядків: {len(unique_rows)}")
print(f"Видалено дублікатів: {duplicates_count}")