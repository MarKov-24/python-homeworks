import random
import os
from sqlalchemy import Column, ForeignKey, Integer, String, Table, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

# Видаляємо стару базу даних при кожному запуску, якщо вона існує
if os.path.exists("school.db"):
  os.remove("school.db")

# Ініціалізація бази даних (створює файл school.db у папці з проєктом)
Base = declarative_base()
engine = create_engine("sqlite:///school.db", echo=False)
Session = sessionmaker(bind=engine)
session = Session()

# 1. Створення моделі даних (Зв'язок "Багато-до-багато")
student_course = Table(
    "student_course",
    Base.metadata,
    Column(
        "student_id", Integer, ForeignKey("students.id"), primary_key=True
    ),
    Column("course_id", Integer, ForeignKey("courses.id"), primary_key=True),
)


class Student(Base):
  __tablename__ = "students"
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String, nullable=False)
  courses = relationship(
      "Course", secondary=student_course, back_populates="students"
  )


class Course(Base):
  __tablename__ = "courses"
  id = Column(Integer, primary_key=True, autoincrement=True)
  title = Column(String, nullable=False)
  students = relationship(
      "Student", secondary=student_course, back_populates="courses"
  )


# Створюємо таблиці в БД
Base.metadata.create_all(engine)

# Генерація 5 курсів та 20 студентів із рандомним розподілом
course_titles = [
    "Математика",
    "Фізика",
    "Програмування",
    "Історія",
    "Англійська",
]
courses = [Course(title=t) for t in course_titles]
session.add_all(courses)
session.commit()

for i in range(1, 21):
  student = Student(name=f"Студент_{i}")
  student.courses = random.sample(courses, random.randint(1, 3))
  session.add(student)
session.commit()
print("--- 1. Базу даних успішно створено та заповнено початковими даними ---")


# 2. Виконання базових операцій (Додавання нового студента)
new_student = Student(name="Іван Іваненко")
math_course = session.query(Course).filter_by(title="Математика").first()
new_student.courses.append(math_course)
session.add(new_student)
session.commit()
print(f"--- 2. Додано нового студента: {new_student.name} ---")


# 3. Запити до бази даних
print("\n--- 3. Запити до бази даних ---")
# А) Студенти конкретного курсу
target_course = session.query(Course).filter_by(title="Математика").first()
print(f"Студенти на курсі '{target_course.title}':")
for s in target_course.students:
  print(f"  * {s.name}")

# Б) Курси конкретного студента (з виправленим іменем)
target_student = (
    session.query(Student).filter_by(name="Іван Іваненко").first()
)
if target_student:
  print(f"\nКурси студента {target_student.name}:")
  for c in target_student.courses:
    print(f"  * {c.title}")
else:
  print("\nСтудента не знайдено!")


# 4. Оновлення та видалення даних
print("\n--- 4. Оновлення та видалення даних ---")
# Оновлення імені студента
student_to_update = session.query(Student).filter_by(name="Студент_1").first()
if student_to_update:
  student_to_update.name = "Олександр Оновлений"
  session.commit()
  print("Студента '_Студент_1' перейменовано на 'Олександр Оновлений'.")

# Видалення студента з бази
student_to_delete = session.query(Student).filter_by(name="Студент_2").first()
if student_to_delete:
  session.delete(student_to_delete)
  session.commit()
  print("Студента 'Студент_2' успішно видалено з бази даних.")