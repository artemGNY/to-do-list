# 📝 To-Do List App
tasks = []

def show_tasks():
    if not tasks:
        print("Список задач пуст ✅")
    else:
        print("Твои задачи:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Введите новую задачу: ")
    tasks.append(task)
    print("Задача добавлена ✅")

def remove_task():
    show_tasks()
    try:
        n = int(input("Введите номер задачи для удаления: "))
        removed = tasks.pop(n - 1)
        print(f"Задача '{removed}' удалена ❌")
    except (ValueError, IndexError):
        print("Неверный номер задачи!")

while True:
    print("\nВыбери действие:")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Удалить задачу")
    print("4. Выход")
    choice = input(">>> ")
    if choice == "1":
        show_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Пока! 🎉")
        break
    else:
        print("Неверный выбор, попробуй снова.")