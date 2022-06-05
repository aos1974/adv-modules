#
# Определение глобальных переменных и констант
#

# МРОТ
MIN_SALARY = 13890

#
# Глобальные функции модуля
#

def calculate_salary(employee_id: int) -> float:
    
    print('Calculating salary...')
    
    salary = 0

    # проверяем табельный номер сотрудника
    if employee_id > 0:
        salary = MIN_SALARY

    return salary
