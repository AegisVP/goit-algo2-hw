from typing import List, Dict
from dataclasses import dataclass

@dataclass
class PrintJob:
    id: str
    volume: float
    priority: int
    print_time: int

@dataclass
class PrinterConstraints:
    max_volume: float
    max_items: int

def optimize_printing(print_jobs: List[PrintJob], constraints: PrinterConstraints) -> Dict:
    """
    Оптимізує чергу 3D-друку згідно з пріоритетами та обмеженнями принтера

    Args:
        print_jobs: Список завдань на друк
        constraints: Обмеження принтера

    Returns:
        Dict з порядком друку та загальним часом
    """

    #### Start of my code

    constraints = PrinterConstraints(constraints["max_volume"], constraints["max_items"])

    print_order = []
    print_jobs_sorted = {}
    total_time = 0

    for print_job in print_jobs:
        priority = print_job.priority
        if priority not in print_jobs_sorted:
            print_jobs_sorted[priority] = []
        # end if
        print_jobs_sorted[priority].append(print_job)
    # end for

    batch = []
    print_volume_remain = constraints.max_volume
    have_jobs_to_print = True
    while have_jobs_to_print:
        added_job = False
        have_jobs_to_print = False
        for print_priority_queue in sorted(print_jobs_sorted.keys()):
            for job in print_jobs_sorted[print_priority_queue]:
                if job.volume <= print_volume_remain and len(batch) < constraints.max_items and job not in batch:
                    batch.append(job)
                    added_job = True
                    print_volume_remain -= job.volume
                # end if
            # end for
            if len(print_jobs_sorted[print_priority_queue]) > 0:
                have_jobs_to_print = True
            # end if
        # end for

        if (added_job == False and have_jobs_to_print) or (added_job and have_jobs_to_print == False):
            max_time = 0
            for job in batch:
                print_order.append(job.id)
                p=job.priority
                print_jobs_sorted[p].remove(job)
                max_time = max(max_time, job.print_time)
            # end for
            total_time += max_time
            print_volume_remain = constraints.max_volume
            batch = []
        # end if
    # end while

    #### End of my code

    return {
        "print_order": print_order,
        "total_time": total_time
    }

# Тестування
def test_printing_optimization():
    # Тест 1: Моделі однакового пріоритету
    test1_jobs = [
        PrintJob("M1", 100, 1, 120),
        PrintJob("M2", 150, 1, 90),
        PrintJob("M3", 120, 1, 150)
    ]

    # Тест 2: Моделі різних пріоритетів
    test2_jobs = [
        PrintJob("M1", 100, 2, 120),  # лабораторна
        PrintJob("M2", 150, 1, 90),  # дипломна
        PrintJob("M3", 120, 3, 150)  # особистий проєкт
    ]

    # Тест 3: Перевищення обмежень об'єму
    test3_jobs = [
        PrintJob("M1", 250, 1, 180),
        PrintJob("M2", 200, 1, 150),
        PrintJob("M3", 180, 2, 120)
    ]

    constraints = {
        "max_volume": 300,
        "max_items": 2
    }

    print("Тест 1 (однаковий пріоритет):")
    result1 = optimize_printing(test1_jobs, constraints)
    print(f"Порядок друку: {result1['print_order']}")
    print(f"Загальний час: {result1['total_time']} хвилин")

    print("\nТест 2 (різні пріоритети):")
    result2 = optimize_printing(test2_jobs, constraints)
    print(f"Порядок друку: {result2['print_order']}")
    print(f"Загальний час: {result2['total_time']} хвилин")

    print("\nТест 3 (перевищення обмежень):")
    result3 = optimize_printing(test3_jobs, constraints)
    print(f"Порядок друку: {result3['print_order']}")
    print(f"Загальний час: {result3['total_time']} хвилин")

if __name__ == "__main__":
    test_printing_optimization()

