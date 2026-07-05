from algorithms_sort import AlgorithmsSort
from random_generation import RandomGenerator


aSort = AlgorithmsSort()
rGenerator = RandomGenerator()

"""Начальные настройки генерации массивов случайных чисел"""
size = 10000
low = 1
high = 10000
count = 4

tests = [rGenerator.generate_random_array(size, low, high) for _ in range (count)]

"""Главное меню"""
print("=== Algorithms Benchmark ===")
print(f"Array size: {size}")
print(f"Range: {low} - {high}")
print()
aSort.bubble_sort(tests[0])
aSort.insertion_sort(tests[1])
aSort.selection_sort(tests[2])
aSort.selection_sort_with_copy(tests[3])