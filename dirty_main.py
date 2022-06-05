###########################################################
# Учебный модуль: Профессиональная работа с Python        #
# Домашнее задание к лекции 1.«Import. Module. Package»   #
###########################################################

from application.salary import *
from db.people import *
from datetime import *

#
# Определение глобальных переменных и констант
#

#
# Глобальные функции модуля
#

#
# Главная функция программы
#

def main():
    print(date.today())
    id = get_employees('VASYA')
    sal = calculate_salary(id)

#
# Основная программа
#

if __name__ == '__main__':
    main()
