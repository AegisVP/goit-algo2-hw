from utils.create_schedule import create_schedule, sort_teachers
from data import teachers, classes

if __name__ == '__main__':
    # Виклик функції створення розкладу
    scheduled_teachers = create_schedule(classes, teachers)

    # Виведення розкладу
    if scheduled_teachers:
        teachers = sort_teachers(teachers)
        print("Розклад занять:")
        for teacher in scheduled_teachers:
            print(teacher)
            print(f"   Викладає предмети: {', '.join(teacher.assigned_classes)}\n")
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
