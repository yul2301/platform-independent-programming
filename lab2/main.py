from pathlib import Path
from datetime import datetime

# Создание папки data
data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

# Путь к файлу
file_path = data_folder / "journal.txt"


# Добавление записи
def add_entry():
    print("\n--- Добавление новой записи ---")

    # Проверка даты
    while True:
        date = input("Введите дату (ГГГГ-ММ-ДД): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Ошибка! Неверный формат даты.")

    # Текст наблюдения
    text = input("Введите текст наблюдения: ")

    # Проверка оценки
    while True:
        try:
            rating = int(input("Введите оценку (1-10): "))

            if 1 <= rating <= 10:
                break
            else:
                print("Ошибка! Оценка должна быть от 1 до 10.")

        except ValueError:
            print("Ошибка! Введите целое число.")

    # Сохранение в файл
    with open(file_path, "a", encoding="utf-8") as file:
        file.write(f"{date} | {rating} | {text}\n")

    print("Запись успешно добавлена!")


# Показ записей
def show_entries():
    print("\n--- Все записи ---")

    if not file_path.exists():
        print("Журнал пуст.")
        return

    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if not lines:
        print("Журнал пуст.")
        return

    print("+------------+---------+--------------------------------+")

    total = 0
    count = 0

    for line in lines:
        parts = line.strip().split(" | ")

        if len(parts) == 3:
            date, rating, text = parts

            print(f"| {date} |    {rating}    | {text}")

            total += int(rating)
            count += 1

    print("+------------+---------+--------------------------------+")

    average = total / count

    print("\nСтатистика:")
    print(f"Всего записей: {count}")
    print(f"Средняя оценка: {average:.2f}")


# Очистка журнала
def clear_journal():
    with open(file_path, "w", encoding="utf-8"):
        pass

    print("Журнал очищен!")


# Главное меню
while True:
    print("\n========================================")
    print("        ЖУРНАЛ НАБЛЮДЕНИЙ")
    print("========================================")

    print("1. Добавить запись")
    print("2. Показать все записи")
    print("3. Очистить журнал")
    print("4. Выход")

    choice = input("\nВаш выбор: ")

    if choice == "1":
        add_entry()

    elif choice == "2":
        show_entries()

    elif choice == "3":
        clear_journal()

    elif choice == "4":
        print("Выход из программы.")
        break

    else:
        print("Ошибка! Неверный пункт меню.")
