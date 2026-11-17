import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

tasks = []

def add_task(title):
    if not title:
        print("Ошибка: название задачи не может быть пустым.")
        return
    task = {"id": len(tasks) + 1, "title": title, "done": False}
    tasks.append(task)
    print(f"Задача '{title}' добавлена.")

def list_tasks():
    print("\n--- Список задач ---")
    if not tasks:
        print("Список пуст.")
        return
    for i in range(len(tasks)):
        status = "V" if tasks[i]["done"] else "X"
        print(f"[{status}] ID: {tasks[i]['id']} | {tasks[i]['title']}")
    print("---")

def mark_task_done(task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            print(f"Задача с ID {task_id} выполнена.")
            return
    print("Задача не найдена.")

def delete_task(task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            logging.info(f"Задача с ID {task_id} удалена.")
            return
    logging.error(f"Задача с ID {task_id} не найдена.")

def delete_completed_tasks():
    print("\nУдаление выполненных задач...")
    count = 0
    for task in tasks[:]:        # <-- ДОБАВИТЬ КВАДРАТНЫЕ СКОБКИ
        if task["done"] == True:
            tasks.remove(task)
            count += 1
    print(f"Удалено задач: {count}")

def main():
    while True:
        print("\nМеню:")
        print("1. Добавить задачу")
        print("2. Показать задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу по ID")
        print("5. Удалить все выполненные задачи")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название задачи: ")
            add_task(title)
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            try:
                task_id = int(input("Введите ID задачи: "))
            except ValueError:
                print("Ошибка: ID должен быть целым числом.")
                continue
            mark_task_done(task_id)
        elif choice == '4':
            try:
                task_id = int(input("Введите ID задачи: "))
            except ValueError:
                print("Ошибка: ID должен быть целым числом.")
                continue
            delete_task(task_id)
        elif choice == '5':
            delete_completed_tasks()
        elif choice == '6':
            print("Выход.")
            break
        else:
            print("Неверный ввод.")

if __name__ == "__main__":
    main()