import numpy as np
import unittest

def average_after_min_module(array):
   # Преобразовываем список в numpy массив
   array = np.array(array)
   
   # Находим индекс элемента с минимальным модулем
   min_module_index = np.argmin(np.abs(array))
   
   # Вычисляем и выводим среднее арифметическое элементов, расположенных после минимального по модулю элемента 
   if min_module_index == len(array) - 1:
      # Если минимальный элемент последний в массиве, то ответа не будет
      print('Минимальный элемент модуля — последний, поэтому показывать нечего')
   else:
      avg = np.mean(array[min_module_index+1:])
      print(f"Среднее значение элементов после элемента минимального модуля равно {avg}")

array = [0.1, 0.2, -0.5, 1.0, -0.1, 0.5, 0.3, -0.2] 

average_after_min_module(array)



# Тест
def average_after_min_module(array):
    array = np.array(array)
    min_module_index = np.argmin(np.abs(array))
    if min_module_index == len(array) - 1:
        return None
    else:
        avg = np.mean(array[min_module_index+1:])
        return avg

# Тест кейс
class TestAverageAfterMinModule(unittest.TestCase):

    def test_average_after_min_module(self):
        self.assertEqual(average_after_min_module([0.1, 0.2, -0.5, 1.0, -0.1, 0.5, 0.3, -0.2]), 
                         np.mean([0.5, 0.3, -0.2]))
        self.assertEqual(average_after_min_module([1, 2, 3, 4]), None)
        self.assertEqual(average_after_min_module([-5, 3, 1, -1, -3, 5]), 0)
        # Add more test cases if needed

if __name__ == '__main__':
    unittest.main()
