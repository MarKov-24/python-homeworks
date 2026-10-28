import os
from urllib.parse import quote
import requests

# Базова адреса вашого сервера
BASE_URL = "http://127.0.0.1:8080"

# Використовуємо реальний файл зображення з вашої папки
IMAGE_PATH = "mars_photo1.jpg"

def main():
    # Перевіряємо, чи існує файл перед завантаженням
    if not os.path.exists(IMAGE_PATH):
        print(f"Помилка: файл {IMAGE_PATH} не знайдено у поточній паці!")
        return

    # --- 1. POST: Завантаження зображення на сервер ---
    print("\n--- 1. Виконуємо POST запит (upload) ---")

    filename = os.path.basename(IMAGE_PATH)
    with open(IMAGE_PATH, "rb") as img_file:
        # За документацією параметр для файлу називається 'image'
        files = {"image": (filename, img_file, "image/jpeg")}

        response = requests.post(f"{BASE_URL}/upload", files=files)

    print(f"Статус-код POST: {response.status_code}")
    print(f"Відповідь сервера: {response.json()}")

    if response.status_code != 201:
        print("Помилка завантаження файлу.")
        return

    # Отримуємо URL з відповіді сервера (наприклад: "http://127.0.0.1:8080/uploads/mars_photo1.jpg")
    data = response.json()
    image_url = data.get("image_url")

    # Витягуємо назву файлу з отриманого URL
    uploaded_filename = image_url.split("/")[-1]

    # --- 2. GET: Отримання посилання на файл ---
    print("\n--- 2. Виконуємо GET запит ---")

    # Ім'я файлу повинно бути закодоване згідно з правилами URL
    encoded_filename = quote(uploaded_filename, safe="")
    get_url = f"{BASE_URL}/image/{encoded_filename}"

    # За документацією: повертає JSON, якщо Content-Type рівний text
    headers = {"Content-Type": "text"}

    get_response = requests.get(get_url, headers=headers)
    print(f"Статус-код GET: {get_response.status_code}")
    print(f"Відповідь сервера (JSON): {get_response.json()}")

    # --- 3. DELETE: Видалення файлу з сервера ---
    print("\n--- 3. Виконуємо DELETE запит ---")

    delete_url = f"{BASE_URL}/delete/{encoded_filename}"
    delete_response = requests.delete(delete_url)

    print(f"Статус-код DELETE: {delete_response.status_code}")
    print(f"Відповідь сервера: {delete_response.json()}")

main()