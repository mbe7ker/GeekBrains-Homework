class Stationery:
    title = "Рисование"

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationery):
    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationery):
    def draw(self):
        print("Запуск отрисовки маркером")


a_1 = Stationery()
a_1.draw()

a_2 = Pen()
a_2.draw()

a_3 = Pencil()
a_3.draw()

a_4 = Handle()
a_4.draw()
