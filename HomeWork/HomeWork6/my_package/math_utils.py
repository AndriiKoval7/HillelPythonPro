"""
Реалізуй у файлі math_utils.py функцію, яка обчислює факторіал числа,
а також функцію для знаходження найбільшого спільного дільника двох чисел.
"""
def get_factorial(param) -> "int":
    """
    Function to calculate the factorial of a number
    :param param:
    :return:
    """
    factorial = param
    try:
        for i in range(1, param):
            factorial = factorial * i
    except:
        print("Parameter must be integer!")
    return factorial

def nsd(a, b) -> "int":
    """
    Function to find the greatest common divisor between two integers
    :param a:
    :param b:
    :return:
    """
    try:
        if a % b == 0:
            return b
        else:
            return nsd(b, a % b)
    except:
        print("Parameters must be INTEGERS!")
        return 0
