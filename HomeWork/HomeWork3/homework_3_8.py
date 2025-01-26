class Price:

    @classmethod
    def is_value_price(cls, value):
        if (type(value) == str and value.isnumeric) or type(value) == int or type(value) == float:
            value = float(value)
        else:
            raise ValueError('Price must be correct format!')
        return value

    def __init__(self, price, add_price = 0.00, subtract_price = 0.00, price_for_comparison = 0.00):
        price = self.is_value_price(price)
        if (price > 0):
            self.__price=round(price, 2)
        else:
            raise ValueError('Price must be more then zero!')
        self.__add_price = round(self.is_value_price(add_price), 2)
        self.__subtract_price = round(self.is_value_price(subtract_price), 2)
        self.__price_for_comparison = round(self.is_value_price(price_for_comparison), 2)
        self.__hint = ""

    def add_price_func(self, price_to_add):
        self.__price += round(self.is_value_price(price_to_add), 2)
        self.__hint = f", price increased by {round(price_to_add, 2)}"

    def subtract_price_func(self, price_to_subtract):
        self.__price -= round(self.is_value_price(price_to_subtract), 2)
        self.__hint = f", price reduced by {round(price_to_subtract, 2)}"

    def price_for_comparison_func(self, price_for_comparison):
        self.__price_for_comparison = round(self.is_value_price(price_for_comparison), 2)
        less_more = ""
        if self.__price_for_comparison > self.__price:
            less_more = " more"
        else:
            less_more = " less"
        self.__hint = f", comparison price is {less_more}, and equal {round(price_for_comparison, 2)}"

    def __str__(self):
        return f"Price is {round(self.__price, 2)}{self.__hint}"
        # округлено костильом, краще б мати спеціальний формат для коштів, бо розрахунки не точні. Може підкажете як правильно)


p1 = Price("123.97987")
print(p1)
p1.add_price_func(10.00)
print(p1)
p1.subtract_price_func(30.00)
print(p1)
p1.price_for_comparison_func(125.00)
print(p1)
p1.price_for_comparison_func(75.00)
print(p1)
