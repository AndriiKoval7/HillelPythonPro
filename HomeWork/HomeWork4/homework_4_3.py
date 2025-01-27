"""
3. Збір статистики про зображення
У вас є каталог з великою кількістю зображень. Напишіть ітератор,
який по черзі відкриває кожне зображення (наприклад, за допомогою модуля PIL),
витягує з нього метадані (розмір, формат тощо) і зберігає ці дані у файл CSV.
"""
import os
from PIL import Image
import csv



class ImgInfoIterator:
    def __init__(self, path_dir, file_name):
        self.path_dir = path_dir
        self.file_name = file_name
        self.index = 0
        self.dir_list = []
        self.img_info = []
        self.img_name = ""
        self.img = None

    def __iter__(self):
        return self

    def __next__(self):
        self.dir_list = os.listdir(self.path_dir)
        while self.index < len(self.dir_list):
            self.img_name = self.dir_list[self.index]
            self.img = Image.open(f"{self.path_dir}/{self.img_name}")
            self.img_info.append(self.img_name)
            self.img_info.append(self.img.format)
            self.img_info.append(self.img.size)
            self.img_info.append(self.img.mode)
            self.index += 1
            with open(self.file_name, 'a', encoding = 'utf-8', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter=' ',
                                        quotechar='|', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow(self.img_info)
                self.img_info = []
            return f"{self.img_name} done!"
        raise StopIteration


iii = ImgInfoIterator("images", "img_info.csv")
for i in iii:
    print(i)
filename = 'img_info.csv'
my_file = open(filename, 'r', encoding = 'utf-8')
txt = my_file.readlines()
print(txt)
my_file.close()
