"""
Створіть простий консольний калькулятор, який дозволяє виконувати основні арифметичні операції (+, -, *, /). Реалізуйте у ньому обробку таких винятків:
ZeroDivisionError
ValueError
Створіть власний виняток UnknownOperationError для невідомих операцій.
	Додаткове завдання: додайте можливість роботи з десятковими числами та обробку винятків, пов'язаних із переповненням.
"""
class UnknownOperationError(Exception):
    pass


# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract two numbers
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide two numbers
def divide(a, b):
    return a / b

def validate_available_actions(action, actions_list):
    if not action in actions_list:
        raise UnknownOperationError("Wrong action!")

def validate_calculator_input_data(cid):
    available_actions = ['+', '-', '*', '/']
    cid_list = cid.split(' ')
    if len(cid_list) != 3:
        print("The calculator input must have three components!")
        my_calc_calculate()
    try:
        validate_available_actions(cid_list[1], available_actions)
    except UnknownOperationError as ex:
        print(f'{ex.__class__}: {ex}')
        print(f"{cid_list[1]} is not available action!")
        my_calc_calculate()
    try:
        float(cid_list[0])
        float(cid_list[2])
    except (ZeroDivisionError, TypeError, ValueError) as e:
        print(f"Error: ({e.__class__.__name__}) - {e}")
        my_calc_calculate()

def my_calc_calculate():
    try:
        calc_string = input("Enter three components for calculate through a space,for example (1 + 3) available actions (+, -, *, /) : ")
        validate_calculator_input_data(calc_string)
        cs_list = calc_string.split(' ')
        a = float(cs_list[0])
        b = float(cs_list[2])
        action = cs_list[1]
        match action:
            case '+':
                print(add(a, b))
            case '-':
                print(subtract(a, b))
            case '*':
                print(multiply(a, b))
            case '/':
                print(divide(a, b))
    except OverflowError as ex:
        print(f'OverflowError: {ex}')
    except Exception as ex:
        print(f'{ex.__class__}: {ex}')

my_calc_calculate()
