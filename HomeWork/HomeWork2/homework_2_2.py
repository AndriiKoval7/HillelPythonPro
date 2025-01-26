def call_function(obj, method_name, *args):
    """The function takes an object, a method name as a string,
    and any arguments for that method. It calls the corresponding
    method of the object and returns the result."""

    method = getattr(obj, method_name, None)

    if callable(method):
        print(method(*args))
    else:
        raise AttributeError(f"Method {method_name} not found")


class Calculator:
    """class for example 2"""
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b


calc = Calculator()
print(call_function(calc, "add", 10, 5))  # 15
print(call_function(calc, "subtract", 10, 5))  # 5
