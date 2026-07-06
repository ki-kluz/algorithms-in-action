import random

import numpy as np


def generate_random_array(size=100, low=1, high=100) -> list[int]:
		"""Генератор (классический) массива случайных целых чисел (с повторениями)"""
		return np.random.randint(low, high + 1, size).tolist()

def generate_nearly_sorted(swaps=10, low=1, high=100) -> list[int]:
		"""Генератор частично отсортированного массива"""
		arr = list(range(low, high + 1))
		for _ in range(swaps):
			idx1, idx2 = random.sample(range(high - low + 1), 2)
			arr[idx1], arr[idx2] = arr[idx2], arr[idx1]
		return arr


# print(generate_random_array(1000, 1, 1000))
# print()
# print(generate_nearly_sorted(50, 1, 1000))