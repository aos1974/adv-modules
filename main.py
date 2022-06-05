###########################################################
# Учебный модуль: Профессиональная работа с Python        #
# Домашнее задание к лекции 1.«Import. Module. Package»   #
###########################################################

from application.salary import calculate_salary
from db.people import get_employees
from datetime import date

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
