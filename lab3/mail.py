from pathlib import Path
from datetime import datetime
import json

# Создание папки data
data_folder = Path("data")
data_folder.mkdir(exist_ok=True)

# Путь к JSON-файлу
file_path = data_folder / "tasks.json"


# Загрузка задач
def load_tasks():
    if file_path.exists():
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    return []


# Сохранение задач
def save_tasks(tasks):
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


# Добавление задачи
def add_task(tasks):
    text = input("Введите задачу: ")

    current_time = datetime.now().strftime("%d.%m.%Y %H:%M")

    task = {
        "text": text,
        "created_at": current_time
    }

    tasks.append(task)

    save_tasks(tasks)

    print("Задача добавлена!")


# Просмотр задач
def show_tasks(tasks):
    if not tasks:
        print("Список задач пуст.")
        return

    print("\n--- Список задач ---")

    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['text']}")
        print(f"   Дата создания: {task['created_at']}")


# Удаление задачи
def delete_task(tasks):
    show_tasks(tasks)

    if not tasks:
        return

    try:
        number = int(input("Введите номер задачи для удаления: "))

        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)

            save_tasks(tasks)

            print("Задача удалена!")

        else:
            print("Ошибка! Неверный номер.")

    except ValueError:
        print("Ошибка! Введите число.")


# Главная программа
tasks = load_tasks()

while True:
    print("\n================================")
    print("       МЕНЕДЖЕР ЗАДАЧ")
    print("================================")

    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Удалить задачу")
    print("4. Выход")

    choice = input("\nВаш выбор: ")

    if choice == "1":
        add_task(tasks)

    elif choice == "2":
        show_tasks(tasks)

    elif choice == "3":
        delete_task(tasks)

    elif choice == "4":
        print("Выход из программы.")
        break

    else:
        print("Ошибка! Неверный пункт меню.")
