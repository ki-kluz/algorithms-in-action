import algorithms_sort as aSort
import random_generation as rGenerator


def run_benchmark(count=4, size=10000, low=1, high=10000, swaps=100):
		aSort.times.clear()
		
		"""Подготовка тестовых данных"""
		original_random = rGenerator.generate_random_array(size, low, high)
		original_nearly = rGenerator.generate_nearly_sorted(swaps, low, high)
		tests_random = [original_random.copy() for _ in range(count)]
		tests_nearly = [original_nearly.copy() for _ in range(count)]

		"""Главное меню"""
		print("=== Algorithms Benchmark ===")
		print("\n--- Random arrays ---")
		print(f"Array size: {size}")
		print(f"Range: {low} - {high}\n")

		aSort.bubble_sort(tests_random[0])
		aSort.insertion_sort(tests_random[1])
		aSort.selection_sort(tests_random[2])
		aSort.selection_sort_with_copy(tests_random[3])

		winner = min(aSort.times, key=lambda x: x[1])
		print(f"\nWinner: {winner[0]} ({winner[1]:.3f})")

		print("\n--- Nearly arrays ---")
		aSort.bubble_sort(tests_nearly[0])
		aSort.insertion_sort(tests_nearly[1])
		aSort.selection_sort(tests_nearly[2])
		aSort.selection_sort_with_copy(tests_nearly[3])

		winner = min(aSort.times, key=lambda x: x[1])
		print(f"\nWinner: {winner[0]} ({winner[1]:.3f})")


if __name__ == "__main__":
		run_benchmark()