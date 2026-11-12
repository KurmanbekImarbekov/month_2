class Person:
    def __init__(self, name, birth_day, ocupation, higher_education):
        self.name = name
        self.birthday = birth_day
        self.ocupation = ocupation
        self.eduction = higher_education

    def introduce(self):
        print(
            f"Меня зовут {self.name}, я родился(лась) {self.birthday}, по профессии {self.ocupation}, высшее образование {self.eduction}"
        )


person1 = Person("Alishka", "17.10.2005", "безработный", False)
person2 = Person("Jaka", "08.08.08", "бухгалтер", True)

print(person1.name, person1.birthday, person1.ocupation, person1.eduction)
print(person2.name, person2.birthday, person2.ocupation, person2.eduction)

person1.introduce()
person2.introduce()
