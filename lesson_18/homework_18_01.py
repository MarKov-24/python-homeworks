import requests

BASE_URL = "https://images-api.nasa.gov"

# 1. Пошук зображень, пов'язаних з ровером Curiosity на Марсі
search_url = f"{BASE_URL}/search"
search_params = {
    "q": "Curiosity rover Mars",
    "media_type": "image",
    "page_size": 20
}

print("Виконую пошук зображень у NASA API...")
response = requests.get(search_url, params=search_params)
response.raise_for_status()

data = response.json()

# Дістаємо список елементів (items) із відповіді API
items = data.get("collection", {}).get("items", [])

if not items:
    print("На жаль, нічого не знайдено.")
    exit()

saved_count = 0

# 2. Перебираємо знайдені елементи, щоб отримати їхні nasa_id
for item in items:
    if saved_count >= 2:
        break

    # Отримуємо дані про елемент та його nasa_id
    data_info = item.get("data", [{}])[0]
    nasa_id = data_info.get("nasa_id")

    if not nasa_id:
        continue

    print(f"\nЗнайдено nasa_id: {nasa_id}")

    # 3. Для кожного nasa_id робимо додатковий запит до endpoint-а /asset/{nasa_id}
    asset_url = f"{BASE_URL}/asset/{nasa_id}"
    print(ftop_str := f"Запит списку файлів для: {asset_url}")

    asset_response = requests.get(asset_url)
    if asset_response.status_code != 200:
        print(f"Не вдалося отримати файли для {nasa_id}")
        continue

    asset_data = asset_response.json()
    asset_items = asset_data.get("collection", {}).get("items", [])

    # 4. Шукаємо посилання на .jpg зображення у списку файлів
    jpg_url = None
    for file_item in asset_items:
        href = file_item.get("href", "")
        if href.endswith(".jpg") and "thumb" not in href:
            jpg_url = href
            break

    if not jpg_url:
        print(f"Для {nasa_id} не знайдено підходящого .jpg файлу.")
        continue

    # 5. Скачуємо зображення
    print(f"Скачуємо зображення за посиланням: {jpg_url}")
    img_response = requests.get(jpg_url)

    if img_response.status_code == 200:
        saved_count += 1
        filename = f"mars_photo{saved_count}.jpg"

        # Зберігаємо файл локально у бінарному режимі ("wb")
        with open(filename, "wb") as f:
            f.write(img_response.content)

        print(f"Успішно збережено як {filename}")
    else:
        print(f"Помилка при скачуванні файлу для {nasa_id}")

print("\nГотово! Завдання виконано, файли збережено.")