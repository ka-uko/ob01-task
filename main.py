class Task:
    def __init__(self, description, deadline, is_completed=False):
        self.description = description
        self.deadline = deadline
        self.is_completed = is_completed

    def to_dict(self):
        return {
            'description': self.description,
            'deadline': self.deadline,
            'is_completed': self.is_completed
        }

#список задач
tasks = [
    Task("Сделать домашнее задание", "01.02.2025", is_completed=True),
    Task("Покататься на велосипеде", "02.02.2025", is_completed=False),
    Task("Заменить замок на гараже", "06.02.2025", is_completed=True),
    Task("Купить зелень", "09.02.2025", is_completed=False)
]

# Вывод исходного списка задач
print("Исходный список задач:")
for task in tasks:
    task_info = task.to_dict()
    print(f"Описание задачи: {task_info['description']}, срок: {task_info['deadline']}")

# Разделение задач на выполненные и невыполненные
completed_tasks = [task for task in tasks if task.is_completed]
incomplete_tasks = [task for task in tasks if not task.is_completed]

# Вывод выполненных задач
print("\nВыполненные задачи:")
for task in completed_tasks:
    task_info = task.to_dict()
    print(f"Описание задачи: {task_info['description']}, срок: {task_info['deadline']}")

# Вывод невыполненных задач
print("\nНевыполненные задачи:")
for task in incomplete_tasks:
    task_info = task.to_dict()
    print(f"Описание задачи: {task_info['description']}, срок: {task_info['deadline']}")

