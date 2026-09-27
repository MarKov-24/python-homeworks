class Employee:
    def __init__(self, name, salary, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.salary = salary


class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department


class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language


class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language,
        )
        self.team_size = team_size

tl = TeamLead(
    name="Mariana",
    salary=20000,
    department="IT",
    programming_language="Python",
    team_size=5,
)

print(f"Ім'я: {tl.name}")
print(f"Зарплата: {tl.salary}")
print(f"Відділ: {tl.department}")
print(f"Мова: {tl.programming_language}")
print(f"Розмір команди: {tl.team_size}")