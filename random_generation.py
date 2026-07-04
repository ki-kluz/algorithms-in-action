import random

import numpy as np


class RandomGenerator:
	"""Класс для генерации различных типов числовых списков под тестирование алгоритмов."""
	
	@staticmethod
	def generate_random_array(size=100, low=1, high=100) -> list[int]:
		"""Генератор (классический) массива случайных целых чисел (с повторениями)"""
		return np.random.randint(low, high + 1, size).tolist()
	
	@staticmethod
	def generate_nearly_sorted(size=100, low=1, high=100, swaps=10) -> list[int]:
		"""Генератор частично отсортированного массива"""
		arr = [i for i in range(low, high + 1, size)]
		for _ in range(swaps):
			idx1, idx2 = random.sample(range(size), 2)
			arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
		return arr