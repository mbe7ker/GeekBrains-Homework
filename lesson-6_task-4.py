class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return print("Машина поехала")

    def stop(self):
        return print("Машина остановилась")

    def turn(self, direction):
        self.direction = direction
        return print(f"Машина повернула {direction}")

    def show_speed(self):
        return print(f"Машина едет со скоростью {self.speed}")


class TownCar(Car):
    def _init_(self, speed, name, color, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f"Скорость {self.speed} слишком высокая. Вам необходимо снизить скорость до 60")
        else:
            print(f"Скорость нормальная")


class SportCar(Car):
    def _init_(self, speed, name, color, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def _init_(self, speed, name, color, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f"Скорость {self.speed} слишком высокая. Вам необходимо снизить скорость до 40")
        else:
            print(f"Скорость нормальная")


class PoliceCar(Car):
    def _init_(self, speed, name, color, is_police):
        super().__init__(speed, color, name, is_police)


c_1 = TownCar(70, "White", "Skoda", False)
print(f"TownCar: {c_1.color} {c_1.name} with a speed of {c_1.speed}; police car - {c_1.is_police}")
c_1.go()
c_1.stop()
c_1.turn("налево")
c_1.show_speed()

c_2 = SportCar(150, "Red", "Ferrari", False)
print(f"SportCar: {c_2.color} {c_2.name} with a speed of {c_2.speed}; police car - {c_2.is_police}")
c_2.go()
c_2.stop()
c_2.turn("направо")
c_2.show_speed()

c_3 = WorkCar(80, "Black", "Mercedez", False)
print(f"WorkCar: {c_3.color} {c_3.name} with a speed of {c_3.speed}; police car - {c_3.is_police}")
c_3.go()
c_3.stop()
c_3.turn("на 180 градусов")
c_3.show_speed()

c_4 = PoliceCar(70, "White", "Lada", True)
print(f"PoliceCar: {c_4.color} {c_4.name} with a speed of {c_4.speed}; police car - {c_4.is_police}")
c_4.go()
c_4.stop()
c_4.turn("налево")
c_4.show_speed()
