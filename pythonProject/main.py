class Vehicle:
    def __init__(self, model, make, year):
        self.__model = model
        self.__make = make
        self.__year = year
        self.__engine_started = False
    def start_engine(self):
        self.__engine_started = True
        print("Двигатель запущен")
    def stop_engine(self):
        self.__engine_started = False
        print("Двигатель заглушен")

class Car(Vehicle):
    def __init__(self, model, make, year, num_doors, num_passengers):
        super().__init__(make, model, year)
        self.__num_doors = num_doors
        self.__num_passengers = num_passengers

    def drive(self):
        if self._Vehicle__engine_started:
            print("Автомобиль начал движение")
        else:
            print("Двигатель не запущен. Сначала запустите двигатель")

    def park(self):
        print("Автомобиль припаркован")

class Truck(Vehicle):
    def __init__(self, model, make, year, max_load_capacity):
        super().__init__(make, model, year)
        self.__max_load_capacity = max_load_capacity

    def load_cargo(self):
        print("Грузовик загружен")

    def unload_cargo(self):
        print("Грузовик разгружен")


car = Car("Toyota", "Camry", 2022, 4, 5)
truck = Truck("Ford", "F-150", 2022, 2000)

car.start_engine()
car.drive()
car.park()
car.stop_engine()

truck.start_engine()
truck.load_cargo()
truck.unload_cargo()
truck.stop_engine()
