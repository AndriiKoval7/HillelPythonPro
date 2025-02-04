"""
Створи CSV-файл з даними про студентів, де кожен рядок містить:
Ім'я студента
Вік
Оцінку
------------------
Ім'я,Вік,Оцінка
Петро,21,90
Марина,22,85
Андрій,20,88
------------------
Напиши програму, яка:
Читає дані з CSV-файлу.
Виводить середню оцінку студентів.
Додає нового студента до файлу.
"""
import csv


class MyDialect(csv.Dialect):
    delimiter = ','
    quotechar = '"'
    lineterminator = '\n'
    quoting = csv.QUOTE_ALL


# Register dialect
csv.register_dialect('my_dialect', MyDialect)

# data = [
#     ["Name", "Age", "Rating"],
#     ["Petro", 21, 90],
#     ["Maryna", 22, 85],
#     ["Andrii", 20, 88],
# ]
#
# # Creating csv file with data
# with open("students.csv", "w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile, dialect='my_dialect')
#     writer.writerows(data)

students_list = []
error_msgs = []

def read_students() -> "list":
    """
    read students info from students.csv
    :return:
    """
    reader = csv.DictReader(open('students.csv', encoding='utf-8'), dialect=MyDialect)
    for row in reader:
         students_list.append(row)
    return students_list

def average_student_rating() -> float:
    """
    average student rating from students.csv
    :return:
    """
    sum = 0
    count = 0
    students_list = read_students()
    for sr in students_list:
        sum += float(sr["Rating"])
        count += 1
    return round((sum / count), 2)

def check_is_numbers(name_arg, arg) -> "list":
    """
    function, that check is params a numbers
    :param name_arg:
    :param arg:
    :return:
    """
    is_complete = True
    message = ''
    try:
        arg = float(arg)
        if arg < 0:
            message = f"{name_arg} must be greater than zero"
            is_complete = False
    except:
        message = f"{name_arg} must be number!"
        is_complete = False
    return [str(is_complete), message]

def student_data_validation(s_params) -> "bool":
    """
    Validate params for adding new student
    :param s_params:
    :return:
    """
    is_valid = True
    age = s_params[1]
    rating = s_params[2]
    age_check = check_is_numbers('age', age)
    print(age_check)
    rating_check = check_is_numbers('rating', rating)
    print(rating_check)
    if age_check[0] == 'False':
        error_msgs.append(age_check[1])
        is_valid = False
    if rating_check[0] == 'False':
        error_msgs.append(rating_check[1])
        is_valid = False
    if age % 1 != 0:
        is_valid = False
        error_msgs.append("Age must be an integer!")
    return is_valid

def add_new_student(name, age, rating):
    """adding new student"""
    student_params = [name, age, rating]
    if student_data_validation(student_params) == True:
        with open("students.csv", "a", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, dialect='my_dialect')
            print(student_params)
            writer.writerow(student_params)
            csvfile.close()
    else:
        print("No new student added!")
        for msg in error_msgs:
            print(msg)


print(read_students())
print('Average student rating: ',average_student_rating())
add_new_student("John", 36, '97')
print(read_students())
