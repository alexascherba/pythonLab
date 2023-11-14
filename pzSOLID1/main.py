# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, items):
        self.items = []

    @abstractmethod
    def calculate_total(self):
        pass

class DiscountStrategy:
    @abstractmethod
    def apply_discount(self, total):
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total):
        return total * (1 - self.percentage / 100)

class ServiceStrategy:
    @abstractmethod
    def apply_service(self, total):
        pass

class DeliveryService(ServiceStrategy):
    def apply_service(self, total):
        return total + 5

#class OrderBuilder:
#    def __init__(self):
 #       self.order = Order()

 #   def add_item(self, item_name, item_price):
  #      self.order.add_item(item_name, item_price)
   #     return self

    #def get_order(self):
     #   return self.order

#class OrderCalculator:
 #   def calculate_total(self, order):
  #      return order.calculate_total()

class ConcreteOrder(Order):
    def calculate_total(self):
        total = sum(item[1] for item in self.items)
        return total


items = [("Pizza", 10),("Cola", 2)]
order = ConcreteOrder(items)

discount_strategy = PercentageDiscount(10)

service_strategy = DeliveryService()

#calculator = OrderCalculator()
total = order.calculate_total()
total = discount_strategy.apply_discount(total)
total = service_strategy.apply_service(total)
print("Total for the order: ", total)