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


garden1 = FruitGarden(150, 13, "Яблоки")
garden2 = FruitGarden(50, 5, "Груши")

print("Информация о фруктовых садах до операций:")
print(f"Фруктовый сад: Площадь - {garden1.area} кв. м, Количество деревьев - {garden1.num_trees}, Тип фруктов - {garden1.fruit_type}")
print(f"Фруктовый сад: Площадь - {garden2.area} кв. м, Количество деревьев - {garden2.num_trees}, Тип фруктов - {garden2.fruit_type}")

garden1.add_tree()
garden2.remove_tree()

print("\nИнформация о фруктовых садах после операций:")
print(f"Фруктовый сад: Площадь - {garden1.area} кв. м, Количество деревьев - {garden1.num_trees}, Тип фруктов - {garden1.fruit_type}")
print(f"Фруктовый сад: Площадь - {garden2.area} кв. м, Количество деревьев - {garden2.num_trees}, Тип фруктов - {garden2.fruit_type}")
