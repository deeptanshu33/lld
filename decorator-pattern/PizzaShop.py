from abc import ABC
# abstract pizza class
class BasePizza(ABC):
    NAME = ""
    PRICE = ""

    def get_price(self):
        return self.PRICE

    def get_name(self):
        return self.NAME

#concrete pizza classes
class Margherita(BasePizza):
    NAME = "Margherita Pizza"
    PRICE = 100

class Farmhouse(BasePizza):
    NAME = "Farmhouse Pizza"
    PRICE = 200

# abstract topping class
# inherits from ABC as it is not to be instantiated on its own
class PizzaTopping(BasePizza, ABC):
    NAME = ""
    PRICE = 0
    def __init__(self, pizza:BasePizza):
        self._pizza = pizza

    def get_name(self):
        return self._pizza.get_name() + " + " + self.NAME
    
    def get_price(self):
        return self._pizza.get_price() + self.PRICE


#concrete topping classes
class ExtraCheese(PizzaTopping):
    NAME = "Extra cheese"
    PRICE = 20  

class Jalapeno(PizzaTopping):
    NAME = "Extra jalapeno"
    PRICE = 20
    
class Olives(PizzaTopping):
    NAME = "Extra olives"
    PRICE = 20