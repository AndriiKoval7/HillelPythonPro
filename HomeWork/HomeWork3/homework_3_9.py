class ProductWithGetSet:

    def __init__(self, price):
        if (price > 0):
            self.__price = round(price, 2)
        else:
            raise ValueError('Price must be more then zero!')

    def get_price(self):
        return self.__price

    def set_price(self, price):
        if (price > 0):
            self.__price = round(price, 2)
        else:
            raise ValueError('Price must be more then zero!')

    def __str__(self):
        return f"Price is {self.__price}"


pwg1 = ProductWithGetSet(123)
print(pwg1)
print(pwg1.get_price())
pwg1.set_price(147)
print(pwg1)
print()


class ProductWithProperty:

    def __init__(self, price):
        if (price > 0):
            self.__price = round(price, 2)
        else:
            raise ValueError('Price must be more then zero!')

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if (value > 0):
            self.__price = round(value, 2)
        else:
            raise ValueError('Price must be more then zero!')

    def __str__(self):
        return f"Price is {self.__price}"


pwp1 = ProductWithProperty(256)
print(pwp1)
print(pwp1.price)
pwp1.price = 138
print(pwp1)
# pwp1.price = -138
print()


class PriceDescriptor:
    def __get__(self, instance, price):
        return instance.__dict__.get("price", None)

    def __set__(self, instance, value):
        if (value > 0):
            self.__price = round(value, 2)
        else:
            raise ValueError('Price must be more then zero!')
        instance.__dict__["price"] = value

    def __delete__(self, instance):
        instance.__dict__["price"] = 0.00


class CurrencyDescriptor:
    def __get__(self, instance, currency):
        return instance.__dict__.get("currency", None)

    def __set__(self, instance, value):
        if value in ['usd', 'eur', 'uah']:
            self.__currency = value
            instance.__dict__["currency"] = value
        else:
            raise ValueError("Currency must be in 'usd', 'eur', 'uah'!")

class ProductWithDescriptor:
    price = PriceDescriptor()
    currency = CurrencyDescriptor()

    def __init__(self, price, currency):
        if (price > 0):
            self.__price = round(price, 2)
        else:
            raise ValueError('Price must be more then zero!')
        self.__currency = currency


    def __str__(self):
        return f"Price is {self.__price} {self.__currency}"


pwd1 = ProductWithDescriptor(276, 'uah')
print(pwd1)
print(pwd1.price)
pwd1.price = 186
print(pwd1.price)
pwd1.currency = 'usd'
print(pwd1.currency)
print(pwd1)
print(pwd1.__dict__)
del pwd1.price
print(pwd1.price)
