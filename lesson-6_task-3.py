class Worker:
    name = ""
    surname = ""
    position = ""
    _income = {"wage": 0, "bonus": 0}


class Position(Worker):
    def get_full_name(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        print(f"Сотрудника зовут: {self.name} {self.surname}")
        print(f"Позиция сотрудника: {self.position}")

    def get_total_income(self, wage, bonus):
        self.wage = wage
        self.bonus = bonus
        self._income = {"wage": wage, "bonus": bonus}
        total_income = int(self._income["wage"]) + int(self._income["bonus"])
        print(f"Доход сотрудника с учетом премии: {total_income}")


p = Position()
p.get_full_name("Ivan", "Ivanov", "Manager")
p.get_total_income(100000, 50000)
