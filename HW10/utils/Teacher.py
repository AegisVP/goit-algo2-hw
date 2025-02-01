class Teacher:

  def __init__(self, id, first_name, last_name, age, email, can_teach_subjects):
    self.id = id
    self.first_name = first_name
    self.last_name = last_name
    self.age = age
    self.email = email
    self.can_teach_subjects = can_teach_subjects
    self.assigned_classes = []

  def assign_class(self, subject):
    if subject in self.can_teach_subjects:
      self.assigned_classes.append(subject)

  def __repr__(self):
    return f'{self.first_name} {self.last_name} ({self.age}), може викладати: {self.can_teach_subjects}'

  def __str__(self):
    return self.__repr__()
