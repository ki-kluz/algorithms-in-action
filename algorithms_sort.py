# import ...

class AlgorithmsSort:
	"""Класс, содержащий реализации базовых алгоритмов сортировки."""
	
	@staticmethod
	def bubble_sort(arr):
		"""Алгоритм сортировки пузырьком (Bubble Sort)"""
		return arr
	
	@staticmethod
	def insertion_sort(arr):
		"""Алгоритм сортировки вставками (Insertion Sort)"""
		return arr
	
	@staticmethod
	def selection_sort(arr):
		"""Алгоритм сортировки выбором (Selection Sort) на месте"""
		n = len(arr)
		# i - граница (всё, что левее i уже отсортировано)
		for i in range(n):
			min_idx = i		# Текущий эл-т неотсортированной последовательности - "минимума"
			for j in range(i + 1, n):
				if arr[j] < arr[min_idx]:
					min_idx = j		# Запоминаем индекс нового "минимума"
			# Меняем местами текущий эл-т (i) и найденный минимальный (min_idx)
			arr[i], arr[min_idx] = arr[min_idx], arr[i]
		return arr

	@staticmethod
	def _find_smallest_idx(arr):
		"""Вспомогательный метод: ищет ИНДЕКС минимального эл-та"""
		smallest, smallest_idx = arr[0], 0
		for i in range(len(arr)):
			if arr[i] < smallest:
				smallest, smallest_idx = arr[i], i
		return smallest_idx
	
	@staticmethod
	def selection_sort_with_copy(arr):
		"""Алгоритм сортировки выбором (Selection Sort) через копию"""
		source_arr = arr.copy()
		new_arr = []
		# Пока в исходном массиве есть эл-ты (не пуст)
		while len(source_arr) != 0:
			# Находим индекс минимального эл-та
			smallest_idx = AlgorithmsSort._find_smallest_idx(source_arr)
			# Вырезаем минимум из старого массива (копии) и добавляем в новый
			new_arr.append(source_arr.pop(smallest_idx))
		return new_arr
	

aSort = AlgorithmsSort()
test_arr_01 = [2, 3, 2, 1, 0, 5, 8, 10]
print(aSort._find_smallest_idx(test_arr_01))
print(aSort.selection_sort_with_copy(test_arr_01))
print(aSort.selection_sort(test_arr_01))