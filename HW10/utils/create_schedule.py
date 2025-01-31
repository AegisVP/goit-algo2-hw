import numpy as np

def sort_teachers(teachers):
  sorted_teachers = sorted(teachers, key=lambda teacher: -teacher.age)
  sorted_teachers = sorted(sorted_teachers, key=lambda teacher: len(teacher.can_teach_subjects))
  sorted_teachers.reverse()
  return sorted_teachers

def create_schedule(classes, teachers):
  scheduled_teachers = list()
  sorted_teachers = sort_teachers(teachers)

  for teacher in sorted_teachers:
    for subject in teacher.can_teach_subjects:
      if subject in classes:
        class_idx = classes.index(subject)
        popped_class = classes.pop(class_idx)
        teacher.assign_class(popped_class)
        if (teacher not in scheduled_teachers): scheduled_teachers.append(teacher)

      if len(classes) == 0:
        return scheduled_teachers

  return None