from datetime import datetime


def analyze_heartbeat():
    # Зчитуємо файл построково
    file = open('hblog.txt', 'r', encoding='utf-8')
    lines = file.readlines()
    file.close()

    # 1. Відбираємо рядки з потрібним ключем
    filtered_log = []
    for line in lines:
        if "Key TSTFEED0300|7E3E|0400" in line:
            filtered_log.append(line)

    # 2. Знаходимо час у кожному відібраному рядку
    timestamps = []
    for line in filtered_log:
        pos = line.find("Timestamp ")
        if pos != -1:
            # Витягуємо 8 символів часу після "Timestamp "
            time_str = line[pos + 10: pos + 18]
            # Перетворюємо у формат datetime
            t = datetime.strptime(time_str, "%H:%M:%S")
            timestamps.append(t)

    # Відкриваємо файл hb_test.log для запису результатів
    hb_test = open('hb_test.log', 'w', encoding='utf-8')

    # 3. Аналізуємо значення парами
    for i in range(len(timestamps) - 1):
        current_time = timestamps[i]
        next_time = timestamps[i + 1]

        # Рахуємо різницю в секундах
        diff = (next_time - current_time).total_seconds()

        # На випадок якщо порядок в логах інший
        if diff < 0:
            diff = (current_time - next_time).total_seconds()

        time_formatted = current_time.strftime("%H:%M:%S")

        # Перевіряємо умови завдання
        if diff > 31 and diff < 33:
            hb_test.write(f"WARNING: heartbeat is {diff} sec at {time_formatted}\n")
        elif diff >= 33:
            hb_test.write(f"ERROR: heartbeat is {diff} sec at {time_formatted}\n")

    # Закриваємо файл логу
    hb_test.close()


# Запуск функції
analyze_heartbeat()