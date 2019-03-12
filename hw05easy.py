# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil


# cоздание директорий dir_1 - dir_9 в текущей папке
def creation_d():
    dir_0, n = (input(f'Введите {s}: ') for s in (
        'имя папки для создания, например как в задании Dir_',
        'количество папок, которые необходимо создать, например как в задании 9'))
    n = int(n)
    for i in range(n):
        dir_name = dir_0 + str(i + 1)
        dir_i = os.path.join(os.getcwd(), dir_name)
        try:
            os.mkdir(dir_i)
        except FileExistsError:
            print('Такая директория уже существует')

    # print(os.listdir(os.getcwd()))

# удаление директорий dir_1 - dir_9 в текущей папке
def disposal_d():
    dir_0, n = (input(f'Введите {s}: ') for s in (
        'имя папки для удаления, например как в задании Dir_',
        'количество папок, которые необходимо создать, например как в задании 9'))
    n = int(n)
    for i in range(n):
        dir_name = dir_0 + str(i + 1)
        dir_i = os.path.join(os.getcwd(), dir_name)
        try:
            os.rmdir(dir_i)
        except FileNotFoundError:
            print('Такая директория уже удалена')

    # print(os.listdir(os.getcwd()))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def show_d():
    return print(os.listdir(os.getcwd()))


# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copyfile_example(source, dest):
    try:
        with open(source, 'rb') as src, open(dest, 'wb') as dst:
            copyfileobj_example(src, dst)
    except NameError:
        print('Ошибка имени')




def copyfile_example1(source, dest):
    shutil.copy2(source, dest)
    try:
        copyfile_example(source, dest)
        return
    except NameError:
        print('Ошибка имени')

source = 'hw05easy.py'
dest = 'hw05easy.copy.py'

copyfile_example1(source, dest)
copyfile_example(source, dest)