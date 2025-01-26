import re


regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')


def isValid(email):
    if re.fullmatch(regex, email):
      return True
    else:
      return False


class User:
    def __init__(self, first_name, last_name, email):
        self.__first_name=first_name
        self.__last_name=last_name
        if (isValid(email)):
            self.__email=email
        else:
            raise ValueError('E-mail is not in correct format')

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, value):
        self.__first_name = value

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, value):
        self.__last_name = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if(isValid(value)):
            self.__email = value
        else:
            raise ValueError('E-mail is not in correct format')

    def __str__(self):
        return f"{self.__first_name} {self.__last_name} with e-mail {self.__email}"


u1 = User("John", "Bush", "my_mal@gmail.com")
print(u1)
print(u1.first_name)
#u1.email = "aergaeragr"
u1.first_name = "Ted"
print(u1)
