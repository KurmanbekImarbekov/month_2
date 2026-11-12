class Distance:
    conversion_dict = {"cm": 0.01, "m": 1, "km": 1000}

    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return f"Значение: {self.value}\nИзмерение: {self.unit}"

    def convert(self):
        return self.value * Distance.conversion_dict.get(self.unit, 1)

    def __add__(self, other):
        result = self.convert() + other.convert()
        return Distance(result, "m")

    def __sub__(self, other):
        result = self.convert() - other.convert()
        return Distance(result, "m")


d1 = Distance(10, "m")
d2 = Distance(2, "km")
d3 = Distance(50, "cm")

print(d1)
print(d2)
print(d3)

print("Сложение:", d1 + d2)
print("Вычитание:", d2 - d1)
