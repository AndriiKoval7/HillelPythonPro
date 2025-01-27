"""
2. Ітератор для генерації унікальних ідентифікаторів
Створіть ітератор, який генерує унікальні ідентифікатори (наприклад, на основі UUID або хеш-функції).
Ідентифікатори повинні генеруватися один за одним при кожній ітерації, і бути унікальними.
"""
import random
import uuid

class UuidIterator:
    def __init__(self, count):
        self.count = count
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < self.count:
            self.index += 1
            return str(uuid.uuid1(random.randint(10,10**10)))
        raise StopIteration

uuid_iter = UuidIterator(25)
for this_uuid in uuid_iter:
    print(this_uuid)

