class Employee:
    def __init__(self, fio, position, birth_year, salary):
        self.fio = fio
        self.position = position
        self.birth_year = birth_year
        self.salary = salary

def create_employee():
    fio = input("Введите ФИО сотрудника: ")
    position = input("Введите должность сотрудника: ")
    birth_year = int(input("Введите год рождения сотрудника: "))
    salary = float(input("Введите заработную плату сотрудника: "))
    return Employee(fio, position, birth_year, salary)

def sort_employees_by_salary(employees):
    n = len(employees)
    for i in range(n):
        for j in range(0, n-i-1):
            if employees[j].salary > employees[j+1].salary:
                employees[j], employees[j+1] = employees[j+1], employees[j]

def search_employee_by_fio(employees, fio):
    found_employees = []
    for employee in employees:
        if employee.fio.lower() == fio.lower():
            found_employees.append(employee)
    return found_employees

def modify_employee(employees):
    index = int(input("Введите индекс сотрудника для изменения: "))
    if 0 <= index < len(employees):
        employee = employees[index]
        print(f"Текущие данные для сотрудника {index}:")
        print(f"ФИО: {employee.fio}")
        print(f"Должность: {employee.position}")
        print(f"Год рождения: {employee.birth_year}")
        print(f"Заработная плата: {employee.salary}")
        print("Введите новые данные:")
        employee.fio = input("ФИО: ")
        employee.position = input("Должность: ")
        employee.birth_year = int(input("Год рождения: "))
        employee.salary = float(input("Заработная плата: "))
        print(f"Данные для сотрудника {index} успешно обновлены.")
    else:
        print("Неверный индекс. Изменения не выполнены.")

def delete_employee(employees):
    index = int(input("Введите индекс сотрудника для удаления: "))
    if 0 <= index < len(employees):
        del employees[index]
        print(f"Сотрудник {index} успешно удален.")
    else:
        print("Неверный индекс. Удаление не выполнено.")

def display_employees(employees):
    print("\nСписок сотрудников:")
    print("{:<5} {:<30} {:<20} {:<10} {:<10}".format("Индекс", "ФИО", "Должность", "Год рождения", "Заработная плата"))
    print("-" * 80)
    for i, employee in enumerate(employees):
        print("{:<5} {:<30} {:<20} {:<10} {:<10}".format(i, employee.fio, employee.position, employee.birth_year, employee.salary))
    print(f"\nВсего сотрудников: {len(employees)}")
def main():
    employees = []
    while True:
        print("\nСистема управления сотрудниками")
        print("1. Создать сотрудника")
        print("2. Сортировать сотрудников по зарплате")
        print("3. Поиск сотрудника по ФИО")
        print("4. Изменить данные сотрудника")
        print("5. Удалить сотрудника")
        print("6. Вывести список сотрудников")
        print("7. Выход")
        choice = int(input("Введите номер операции: "))
        if choice == 1:
            employees.append(create_employee())
        elif choice == 2:
            sort_employees_by_salary(employees)
            print("Сотрудники отсортированы по зарплате:")
            display_employees(employees)
        elif choice == 3:
            search_fio = input("Введите ФИО для поиска: ")
            found_employees = search_employee_by_fio(employees, search_fio)
            if found_employees:
                print(f"Найденные сотрудники с ФИО '{search_fio}':")
                display_employees(found_employees)
            else:
                print(f"Сотрудник с ФИО '{search_fio}' не найден.")
        elif choice == 4:
            modify_employee(employees)
        elif choice == 5:
            delete_employee(employees)
        elif choice == 6:
            display_employees(employees)
        elif choice == 7:
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 7.")

def test_employee_management_system():
    test_employees = [Employee("Иванов Иван Иванович", "Аналитик", 1985, 5000),
                      Employee("Петров Петр Петрович", "Программист", 1990, 4500),
                      Employee("Сидоров Алексей Алексеевич", "Дизайнер", 1988, 5500)]

    created_employee = create_employee()
    assert isinstance(created_employee, Employee), "Ошибка: create_employee() должна возвращать объект класса Employee"
    test_employees.append(created_employee)

    sort_employees_by_salary(test_employees)
    sorted_employees = sorted(test_employees, key=lambda x: x.salary)
    print("Отсортированные сотрудники по зарплате:")
    display_employees(sorted_employees)
    sort_test_passed = test_employees == sorted_employees

    search_fio = input("Введите ФИО для поиска: ")
    found_employees = search_employee_by_fio(test_employees, search_fio)
    if found_employees:
        print(f"Найденные сотрудники с ФИО '{search_fio}':")
        display_employees(found_employees)
    else:
        print(f"Сотрудник с ФИО '{search_fio}' не найден.")
    search_test_passed = bool(found_employees)

    modify_employee(test_employees)

    delete_employee(test_employees)

    print("Тест вывода сотрудников:")
    display_employees(test_employees)

    display_test_passed = True 
    all_tests_passed = sort_test_passed and search_test_passed and display_test_passed
    return all_tests_passed

if __name__ == "__main__":
    all_tests_passed = test_employee_management_system()
    if all_tests_passed:
      print("Тест пройден")
    else :
      print("Тест не пройден")
