from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.completed = False  # Статус задачи: выполнена или нет

    def mark_completed(self):
        self.completed = True  # Отметка задачи как выполненной

    def __str__(self):
        # Преобразуем задачу в строку для удобного отображения
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date):
        # Добавляем новую задачу
        task = Task(description, due_date)
        self.tasks.append(task)

    def mark_task_completed(self, description):
        # Находим задачу по описанию и отмечаем её как выполненную
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                print(f"Задача '{description}' отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена.")

    def show_all_tasks(self):
        # Выводим список всех задач
        print("Список всех задач:")
        for task in self.tasks:
            print(task)

    def show_pending_tasks(self):
        # Выводим список только невыполненных задач
        print("Список невыполненных задач:")
        for task in self.tasks:
            if not task.completed:
                print(task)

    def show_completed_tasks(self):
        # Выводим список только выполненных задач
        print("Список выполненных задач:")
        for task in self.tasks:
            if task.completed:
                print(task)

# Пример использования
manager = TaskManager()
manager.add_task("Купить продукты", "2024-10-25")
manager.add_task("Сделать домашнее задание", "2024-10-26")

manager.show_all_tasks()  # Показать все задачи

manager.mark_task_completed("Купить продукты")  # Отметить задачу как выполненную

manager.show_all_tasks()  # Показать все задачи
manager.show_pending_tasks()  # Показать только невыполненные задачи
manager.show_completed_tasks()  # Показать только выполненные задачи

brother = TaskManager()
brother.add_task("Зарядка", "2024-10-30")
brother.add_task("drink water", "2024-10-29")

brother.show_all_tasks()

brother.mark_task_completed("drink water")

brother.show_all_tasks()


