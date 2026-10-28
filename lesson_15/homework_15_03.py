import logging
import xml.etree.ElementTree as ET
from pathlib import Path

# 1. Налаштовуємо логер на рівень INFO із зручним форматом виведення
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger("xml_searcher")


def find_incoming_by_group_number(file_path: Path, target_number: str):
    """Шукає group/number і повертає значення timingExbytes/incoming."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        # Перебираємо всі теги <group> у файлі
        for group in root.findall("group"):
            number_elem = group.find("number")

            # Порівняємо знайдений номер групи з тим, який ми шукаємо
            if number_elem is not None and number_elem.text == str(target_number):
                # Шукаємо шлях timingExbytes/incoming всередині цієї групи
                incoming_elem = group.find("timingExbytes/incoming")
                if incoming_elem is not None:
                    return incoming_elem.text
                else:
                    return "Тег 'incoming' відсутній у цій групі"

        return None  # Якщо групу з таким номером не знайдено

    except Exception as e:
        logger.error(f"Помилка при читанні або парсингу XML: {e}")
        return None


# 2. Вказуємо шлях до вашого файлу groups.xml
xml_path = Path("ideas_for_test/work_with_xml/groups.xml")

# 3. Вказуємо номер групи, яку хочемо знайти (наприклад, "2" або "0")
search_number = "4"

# Викликаємо функцію пошуку
result = find_incoming_by_group_number(xml_path, search_number)

# 4. Виводимо результат у консоль через логер на рівні INFO
if result:
    logger.info(f"Значення timingExbytes/incoming для групи {search_number}: {result}")
else:
    logger.info(f"Групу з номером {search_number} не знайдено.")