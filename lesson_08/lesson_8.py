class Student:
    def __init__(self, first_name, second_name, age, average_grade):
        self.first_name=first_name
        self.second_name=second_name
        self.age=age
        self.average_grade=average_grade

    def update_average_grade(self, new_grade):
        self.average_grade= new_grade

    def display_info(self):
        print(f"Student: {self.first_name} {self.second_name}")
        print(f"Age: {self.age}")
        print(f"Average grade: {self.average_grade}")

student1 = Student("Петро", "Петренко", 40, 18)
print("---Дані про Петра---")
student1.display_info()

student1.update_average_grade(30)
print("---Дані після зміни середнього балу---")
student1.display_info()

