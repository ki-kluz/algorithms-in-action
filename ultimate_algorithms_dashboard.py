from algorithms_sort import AlgorithmsSort
from random_generation import RandomGenerator


aSort = AlgorithmsSort()
rGenerator = RandomGenerator()

"""Начальные настройки генерации массивов случайных чисел"""
size = 100
low = 1
high = 100
count = 4

tests = [rGenerator.generate_random_array(size, low, high) for _ in range (count)]

"""Главное меню"""
print("=== Algorithms Benchmark ===")
print(f"Array size: {size}")
print(f"Range: {low} - {high}")
print()
print(aSort.bubble_sort(tests[0]))
print(aSort.insertion_sort(tests[1]))
print(aSort.selection_sort(tests[2]))
print(aSort.selection_sort_with_copy(tests[3]))