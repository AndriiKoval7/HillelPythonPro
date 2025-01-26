import inspect


def analyze_object(obj):
    """A function that takes any object and outputs:
    the type of the object,
    a list of all the object's methods and attributes,
    and the type of each attribute."""

    print("Тип об'єкта: ", type(obj))
    print('Атрибути і методи:')
    for name, data in inspect.getmembers(obj):
        if name.startswith('__'):
            continue
        print('- {} : {!r}'.format(name, type(data)))


class MyClass:
    """class for example"""
    def __init__(self, value):
        self.value = value

    def say_hello(self):
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)

