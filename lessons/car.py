class Car:
    def __init__(self, marka, color):
        self.marka = marka
        self.color = color
    def drive_to(self, destin):
        print(f'Машина марки {self.marka} едет в {destin}')


car1 = Car("mers",'black')
car2 = Car("bmw", "white")
print(car1.marka,car2.marka)
car2.drive_to('Osh')


class Hero:
    def __init__(self, name, level, force):
        self.name = name
        self.level = level
        self.force = force
    def attack(self, weapon):
        print(f'Герой по имени {self.name} атакует с помощью {weapon}')

hero1 = Hero("Valkyria",15,'woodcutter')
hero2 = Hero("Knight", 13, 'khigth')
print(hero1.name)
hero1.attack("Topor")