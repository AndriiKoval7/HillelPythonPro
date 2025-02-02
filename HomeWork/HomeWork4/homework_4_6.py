"""
Напишіть ітератор, який буде повертати всі файли в заданому каталозі по черзі.
Для кожного файлу виведіть його назву та розмір.
"""
import os
the_path = os.getcwd()


class FileFoundIterator:
    def __init__(self, list_files):
        self.list_files = list_files
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.list_files) - 1:
            self.index += 1
            file_name = self.list_files[self.index]
            file_size = os.path.getsize(f'{the_path}/{file_name}')
            return f"file name: {file_name}, file size: {file_size}"
        raise StopIteration


# files in directory
dir_list = os.listdir(the_path)
print(f"Files in directory: {the_path}")
files_dict = FileFoundIterator(dir_list)
for item in files_dict:
    print(item)
