class Employee:
    def __init__(self, full_name, position, birth_year, salary):
        self.full_name = full_name
        self.position = position
        self.birth_year = birth_year
        self.salary = salary

    def __repr__(self):
        return f"{self.full_name}, {self.position}, {self.birth_year}, {self.salary}"


def create_employee():
    full_name = input("Введите ФИО сотрудника: ")
    position = input("Введите должность сотрудника: ")
    birth_year = int(input("Введите год рождения сотрудника: "))
    salary = float(input("Введите заработную плату сотрудника: "))
    return Employee(full_name, position, birth_year, salary)


def sort_employees_by_salary(employees):
    return sorted(employees, key=lambda x: x.salary)


def find_employee_by_position(employees, position):
    found_employees = [employee for employee in employees if employee.position == position]
    return found_employees


def update_employee(employees, index):
    if 0 <= index < len(employees):
        employees[index] = create_employee()
        print("Данные сотрудника обновлены.")
    else:
        print("Неверный индекс.")


def delete_employee(employees, index):
    if 0 <= index < len(employees):
        del employees[index]
        print("Сотрудник удалён.")
    else:
        print("Неверный индекс.")


def display_employees_table(employees):
    print("Список сотрудников:")
    print("№ | ФИО              | Должность         | Год рождения | Заработная плата")
    print("-" * 70)
    for i, employee in enumerate(employees, 1):
        print(f"{i} | {employee.full_name:<17} | {employee.position:<17} | {employee.birth_year:^13} | {employee.salary:^16}")
    print("-" * 70)
    print(f"Всего сотрудников: {len(employees)}")


def run_unit_tests():
    # Тест создания объекта Employee
    emp1 = Employee("Иванов Иван", "Программист", 1990, 50000)
    assert repr(emp1) == "Иванов Иван, Программист, 1990, 50000", "Тест создания объекта Employee не пройден"

    # Тест сортировки по заработной плате
    employees = [Employee("Иванов Иван", "Программист", 1990, 50000),
                 Employee("Петров Петр", "Менеджер", 1985, 60000),
                 Employee("Сидоров Сидор", "Бухгалтер", 1995, 40000)]
    sorted_employees = sort_employees_by_salary(employees)
    assert sorted_employees == [employees[2], employees[0], employees[1]], "Тест сортировки по заработной плате не пройден"

    print("Все тесты пройдены успешно.")


if __name__ == "__main__":
    # Запуск юнит-тестов
    run_unit_tests()

    employees_list = []

    while True:
        print("\nМеню:")
        print("1. Создать нового сотрудника")
        print("2. Сортировка списка сотрудников по зарплате")
        print("3. Поиск сотрудника по должности")
        print("4. Изменить данные сотрудника")
        print("5. Удалить сотрудника")
        print("6. Вывести список сотрудников")
        print("7. Завершить программу")

        choice = input("Выберите действие: ")

        if choice == "1":
            employees_list.append(create_employee())
        elif choice == "2":
            employees_list = sort_employees_by_salary(employees_list)
        elif choice == "3":
            position = input("Введите должность для поиска: ")
            found_employees = find_employee_by_position(employees_list, position)
            display_employees_table(found_employees)
        elif choice == "4":
            index = int(input("Введите номер сотрудника для изменения его данных: ")) - 1
            update_employee(employees_list, index)
        elif choice == "5":
            index = int(input("Введите номер сотрудника для удаления: ")) - 1
            delete_employee(employees_list, index)
        elif choice == "6":
            display_employees_table(employees_list)
        elif choice == "7":
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие из списка.")
