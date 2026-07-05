import time


def calculation_of_algorithm_speed(name: str):			# Подсчёт скорости выполнения алгоритма (декоратор)
		def decorator(func):
			def wrapper(arr):
				start_time = time.perf_counter()
				res = func(arr)
				end_time = time.perf_counter()
				print(f"{name}: {end_time - start_time:.3f} sec")
				return res
			return wrapper
		return decorator

class AlgorithmsSort:
	"""Класс, содержащий реализации базовых алгоритмов сортировки."""
	
	@staticmethod
	@calculation_of_algorithm_speed("Bubble Sort")
	def bubble_sort(arr):
		"""Алгоритм сортировки пузырьком (Bubble Sort)"""
		n = len(arr)
		for i in range(n):
			# Начинаем с 0 (ВСЕГДА):
			# - i нужен, чтобы не лезть в уже отсортированную половину (конец)
			# - 1 нужен, чтобы при j + 1 не вылететь за границы массива
			for j in range(0, n - i - 1):
				# Сравниваем парные эл-ты
				if arr[j] > arr[j + 1]:
					arr[j], arr[j + 1] = arr[j + 1], arr[j]
		return arr
	
	@staticmethod
	@calculation_of_algorithm_speed("Insertion Sort")
	def insertion_sort(arr):
		"""Алгоритм сортировки вставками (Insertion Sort)"""
		n = len(arr)
		# Начинаем со ВТОРОГО, тк ПЕРВЫЙ сам по себе отсортирован
		for i in range(1, n):
			j = i
			# Пока не дошли до начала И левый эл-т > правого
			while j > 0 and arr[j - 1] > arr[j]:
				arr[j], arr[j - 1] = arr[j - 1], arr[j]
				j -= 1		# Сдвигаем индекс j влево вслед за элементом
		return arr
	
	@staticmethod
	@calculation_of_algorithm_speed("Selection Sort (In-Place)")
	def selection_sort(arr):
		"""Алгоритм сортировки выбором (Selection Sort) на месте"""
		n = len(arr)
		# i - граница (всё, что левее i уже отсортировано)
		for i in range(n):
			min_idx = i		# Текущий эл-т неотсортированной последовательности - "минимум"
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
	@calculation_of_algorithm_speed("Selection Sort (With-Copy)")
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