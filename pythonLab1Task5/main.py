class FruitGarden:
    def __init__(self, area, num_trees, fruit_type):
        self.area = area
        self.num_trees = num_trees
        self.fruit_type = fruit_type

    def add_tree(self):
        self.num_trees += 1

    def remove_tree(self):
        if self.num_trees > 0:
            self.num_trees -= 1
    def print_inf(self):
        print(f"Фруктовый сад: Площадь - {self.area} кв. м, Количество деревьев - {self.num_trees}, Тип фруктов - {self.fruit_type}")

class AppleGarden(FruitGarden):
    def __init__(self, area, num_trees):
        super().__init__(area, num_trees, "Яблони")
    def print_inf(self):
        print(f"Фруктовый сад: Площадь - {self.area} кв. м, Количество деревьев - {self.num_trees}, Тип фруктов - {self.fruit_type}")
        print(f"Тут выводится информация только о яблонях")

class PearGarden(FruitGarden):
    def __init__(self, area, num_trees):
        super().__init__(area, num_trees, "Груши")
    def print_inf(self):
        print(f"Фруктовый сад: Площадь - {self.area} кв. м, Количество деревьев - {self.num_trees}, Тип фруктов - {self.fruit_type}")
        print(f"Тут выводится информация только о грушах")

garden3 = AppleGarden(25, 7)
garden4 = PearGarden(45, 16)

print("Информация о фруктовых садах до операций:")
garden3.print_inf()
garden4.print_inf()

garden3.add_tree()
garden4.remove_tree()

print("Информация о фруктовых садах после операций:")
garden3.print_inf()
garden4.print_inf()
