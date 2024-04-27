class State:
  def __init__(self, name, capital, population, area):
    self.name = name
    self.capital = capital
    self.population = population
    self.area = area

  def get_population_density(self):
    try:
        return self.population / self.area
    except ZeroDivisionError:
        return 0
def add_new_state(states):
  # Запрашиваем информацию о новом государстве у пользователя
  name = input("Введите название государства: ")
  capital = input("Введите столицу государства: ")
  population = int(input("Введите численность населения государства(Млн. чел.): "))
  area = float(input("Введите площадь государства(Млн. Км²): "))

  # Создаем новый объект State
  new_state = State(name, capital, population, area)

  # Добавляем новый объект в список
  states.append(new_state)

  # Подтверждение добавления
  print(f"Государство {name} добавлено в список!")

def sort_by_density(states):
  # Sort the 'states' list in-place
  states.sort(key=lambda state: state.get_population_density(), reverse=True)
  print("Государства отсортированы по плотности населения:")
  print_table(states)

def find_by_param(states, param_name, param_value):
  found_states = []
  for state in states:
    if getattr(state, param_name) == param_value:
      found_states.append(state)
  return found_states

def search_and_print_table(states):
  # Запрос у пользователя значения для поиска
  search_term = input("Введите название государства для поиска: ")

  # Поиск по названию
  filtered_states = [state for state in states if search_term.lower() in state.name.lower()]

  # Печать таблицы
  print_table(filtered_states)

def change_element(states, index):
  if 0 <= index < len(states):
    # Запрашиваем новые данные у пользователя
    new_name = input("Введите новое название: ")
    new_capital = input("Введите новую столицу: ")
    new_population = int(input("Введите новую численность населения: "))
    new_area = float(input("Введите новую площадь: "))

    # Изменяем данные элемента
    states[index].name = new_name
    states[index].capital = new_capital
    states[index].population = new_population
    states[index].area = new_area

    print(f"Данные элемента с индексом {index} успешно изменены!")
  else:
    print(f"Индекс {index} выходит за пределы списка!")

def delete_element(states, index):
  if 0 <= index < len(states):
    del states[index]
    print(f"Элемент с индексом {index} успешно удален!")
  else:
    print(f"Индекс {index} выходит за пределы списка!")

def print_table(states):
  # Заголовки таблицы
  headers = ["Название", "Столица", "Население", "Площадь", "Плотность населения"]
  print("-" * len(" ".join(headers)))
  print("{:15} {:15} {:10} {:10} {:15}".format(*headers))
  print("-" * len(" ".join(headers)))

  # Вывод строк таблицы с нумерацией
  for i, state in enumerate(states, 1):
    population_density = state.get_population_density()
    print(f"{i:3} {state.name:15} {state.capital:15} {state.population:10} {state.area:10.2f} {population_density:15}")
  print("-" * len(" ".join(headers)))
  print(f"Общее количество: {len(states)}")

states = []  # Список объектов State

while True:
  print()
  print("1. Добавить новое государство")
  print("2. Отсортировать государства по плотности населения")
  print("3. Найти государство")
  print("4. Изменить данные государства")
  print("5. Удалить государство")
  print("6. Выводить данные в виде таблицы")
  print("0. Выйти из программы")

  action = input("Выберите действие: ")

  try:
      if action == "1":
          add_new_state(states)
      elif action == "2":
          sort_by_density(states)
          print_table(states)
      elif action == "3":
          search_and_print_table(states)
      elif action == "4":
          name = input("Введите название государства: ")
          for i, state in enumerate(states):
              if state.name.lower() == name.lower():
                  change_element(states, i)
                  break
          else:
              print("Государство не найдено!")
      elif action == "5":
          name = input("Введите название государства: ")
          for i, state in enumerate(states):
              if state.name.lower() == name.lower():
                  delete_element(states, i)
                  break
          else:
              print("Государство не найдено!")
      elif action == "6":
          print_table(states)
      elif action == "0":
          break
      else:
          print("Неизвестное действие")

  except ValueError as e:
      print(f"Произошла ошибка: {e}. Пожалуйста, попробуйте снова.")
