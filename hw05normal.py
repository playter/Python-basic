# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys
import shutil
import hw05easy


def what_do():
	choice = int(input('Выберите один из пунктов меню\n'
				  '1. Перейти в папку\n'
				  '2. Просмотреть содержимое текущей папки\n'
				  '3. Удалить папку\n'
				  '4. Создать папку\n'
				  'Ваш выбор: ', ))

	if choice == 1:
		dir_choice = input('Укажите название папки с  // (двойной дробью)', )
		os.chdir(dir_choice)
	elif choice == 2:
	    hw05easy.show_d()
	elif choice == 3:
	    hw05easy.disposal_d()
	elif choice == 4:
	    hw05easy.creation_d()
	else:
	    print('Введен не существующий пункт меню! Попробуйте вновь.')

what_do()

