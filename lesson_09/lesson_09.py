class Romb:
    def __init__(self, storona_a: float, kut_a: float):
        self.storona_a = storona_a
        self.kut_a = kut_a

    def __setattr__(self, name, value):
        if name == "storona_a":
            if value <= 0:
                raise ValueError("Сторона а повинна бути більше 0")
            super().__setattr__(name, value)

        elif name == "kut_a":
            if value <= 0 or value >= 180:
                raise ValueError("Кут а повинен бути в межах від 0 до 180 градусів")

            super().__setattr__("kut_a", value)
            super().__setattr__("kut_b", 180 - value)

        elif name == "kut_b":
            if "kut_a" in self.__dict__ and value != (180 - self.kut_a):
                raise AttributeError("Кут б обчислюється автоматично з кута а і не змінюється вручну")
            super().__setattr__(name, value)

        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Ромб: сторона a = {self.storona_a}, кут a = {self.kut_a} deg, кут b = {self.kut_b} deg"

print("=== Створення об'єкта ===")
r = Romb(10, 60)
print(r)
print("Перевірка суми кутів (180):", r.kut_a + r.kut_b == 180)

print("\n=== Зміна кута a ===")
r.kut_a = 45
print("Новий кут a:", r.kut_a)
print("Автоматично перерахований кут b:", r.kut_b)

print("\n=== Перевірка помилок ===")

try:
    r.storona_a = -5
except ValueError as e:
    print("Помилка сторони:", e)

try:
    r.kut_a = 200
except ValueError as e:
    print("Помилка кута:", e)

try:
    r.kut_b = 90
except AttributeError as e:
    print("Помилка при зміні кута b:", e)