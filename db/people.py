#
# Определение глобальных переменных и констант
#

#
# Глобальные функции модуля
#

# поиск сотрудника по ФИО
def get_employees(name: str) -> int:

    print('Getting employee ID from DB..')

    if len(name) > 0:
        employee_id = 1
    else:
        employee_id = 0

    return employee_id

