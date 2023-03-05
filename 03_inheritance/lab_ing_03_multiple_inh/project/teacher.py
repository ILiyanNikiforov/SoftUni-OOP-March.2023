from project.employee import Employee
from project.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."

# my_teacher = Teacher()
# print(my_teacher.teach())
# print(my_teacher.get_fired())
# print(my_teacher.sleep())