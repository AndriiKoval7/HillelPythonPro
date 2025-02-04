"""
У файлі string_utils.py реалізуй функції для:
Перетворення тексту в верхній регістр.
Видалення пробілів на початку та в кінці рядка.
"""
def str_to_uppercase(str_param) -> "str":
    """
    Function to make string with uppercase
    :param str_param:
    :return:
    """
    return str(str_param).upper()

def del_empty_spaces(str_par) -> "str":
    """
    Function to remove spaces at the beginning and end of a string
    :param str_par:
    :return:
    """
    return str_par.strip()