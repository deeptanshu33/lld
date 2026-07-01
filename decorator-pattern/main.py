from PizzaShop import Margherita, Farmhouse, ExtraCheese, Jalapeno, Olives

# margherita with extra cheese
pizza = ExtraCheese(Margherita())
print(pizza.get_name())
print(pizza.get_price())
print("--------------------------------------")

# farmhouse with extra cheese + olives
pizza2 = Olives(ExtraCheese(Farmhouse()))
print(pizza2.get_name())
print(pizza2.get_price())
print("--------------------------------------")

#margherita with extra cheese and jalapeno
pizza3 = ExtraCheese(Jalapeno(Margherita()))
print(pizza3.get_name())
print(pizza3.get_price())