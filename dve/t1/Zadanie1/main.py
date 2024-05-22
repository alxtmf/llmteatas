import re
from datetime import datetime
def is_valid_date(date_str):
    pattern = r"^(0[1-9]|[12][0-9]|3[01])([./])(0[1-9]|1[0-2])\2(\d{4})$"
    match = re.match(pattern, date_str)
    if not match:
        return False
    day, sep, month, year = match.groups()
    try:
        datetime.strptime(f"{day}{sep}{month}{sep}{year}", f"%d{sep}%m{sep}%Y")
    except ValueError:
        return False

    return True
if __name__ == "__main__":
    date_str = input("Введите дату в формате dd/mm/yyyy или dd.mm.yyyy: ")
    if is_valid_date(date_str):
        print("Дата введена правильно.")
    else:
        print("Дата введена неправильно.")
    test_dates = {
        "31/12/2020": True,
        "01.01.2021": True,
        "31/04/2020": False,  # Апрель 30 дней
        "32/01/2020": False,  # Нет 32 числа
        "01-01-2021": False  # Неправильный разделитель
    }
    all_tests_passed = True
    for date, expected in test_dates.items():
        result = is_valid_date(date)
        if result != expected:
            all_tests_passed = False
            break
    if all_tests_passed:
        print("тест пройден.")
    else:
        print("тест не пройден.")
