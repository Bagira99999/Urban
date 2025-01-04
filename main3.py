
class Car:
    def __init__(self, model, year_of_release, engine_capacity, price, mileage, number_of_wheels=4):
        self.model = model
        self.year_of_release = year_of_release
        self.engine_capacity = engine_capacity
        self.price = price
        self.mileage = mileage
        self.number_of_wheels = number_of_wheels
        print( "Машина")

    def descrition(self):
        description = (f"Модель - {self.model}, Год выпуска - {self.year_of_release}, Объем двигателя - "
                      f"{self.engine_capacity}, Цена - {self.price}, Пробег - {self.mileage}, Количество колес - "
                      f"{self.number_of_wheels}")
        return description

corvette = Car("Модель", "Год выпуска", "Объем двигателя", "Цена",
               "Пробег", 4)

class Truck(Car):
    def __init__(self, model, year_of_release, engine_capacity, price, mileage, number_of_wheels=8):
        super().__init__(model, year_of_release, engine_capacity, price, mileage, number_of_wheels)
        self.car_group = "Грузовик"

Kenworth = Truck("Модель", "Год выпуска", "Объем двигателя", "Цена",
                 "Пробег", 8)

print(corvette.descrition())
print(Kenworth.descrition())

