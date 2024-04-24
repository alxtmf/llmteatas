import re
from datetime import datetime
def is_valid_date(date_str):
    date_pattern = re.compile(r'^([0-2][0-9]|3[0-1])[./]([0][1-9]|1[0-2])[./](\d{4})$')
    if not re.match(date_pattern, date_str):
        return False
    day, month, year = map(int, re.split('[./]', date_str))
    try:
        datetime(year, month, day)
    except ValueError:
        return False
    return True
while True:
        date_input = input("Введите дату рождения: ")
        if is_valid_date(date_input):
            print("Дата рождения: " + date_input)
            break
        else:
            print("Введенная дата некорректна. Попробуйте снова.")
import time
time.sleep(5)

