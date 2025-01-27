"""
1. Створення власного ітератора для зворотного читання файлу
Напишіть власний ітератор, який буде зчитувати файл у зворотному порядку —
рядок за рядком з кінця файлу до початку. Це може бути корисно для аналізу лог-файлів,
коли останні записи найважливіші.
"""
class FileReadBackwardsIterator:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter < len(self.text):
            some_row = self.text[self.index]
            self.index -= 1
            self.counter += 1
            return some_row
        raise StopIteration


filename = 'my_text.txt'
text_file = open(filename, 'r', encoding = 'utf-8')
txt = text_file.readlines()
string_iter = FileReadBackwardsIterator(txt)
for this_row in string_iter:
    print(this_row)

text_file.close()