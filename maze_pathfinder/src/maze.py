import random
from collections import deque

import numpy as np

"""
ИНФОРМАЦИЯ:
Лабиринт - матрица заданной размерности (rows × cols)

Основная логика строится вокруг понятия "комната"...
	Пример:
		  0 1 2
		0 # # #
		1 # _ #
		2 # # #
...она может быть:
	- "посещенной" - комната, в которой были;
	- "не посещенной" - комната, в которой не были;

Генерация начальной матрицы (лабиринта) подразумевает, что все комнаты не посещенные (их координаты - все четные строки/столбцы)

Стек в нашем случае выступает в роли памяти, истории пути по лабиринту(*) =>
=> так мы сможем возвращаться до ближайшей "развилки" (- комнаты, у которой есть не посещенные соседи)
"""

class Stack:
		def __init__(self):
			self._items = deque()

		def size(self):
			return len(self._items)
		
		def is_empty(self):
			return self.size() == 0
		
		def push(self, item):
			self._items.append(item)

		def pop(self):
			if not self.is_empty():
				return self._items.pop()
			return None

# stack = Stack()

# print(stack)								# Вывести объект stack (напр. <__main__.Stack object at 0x1009a6250>)
# print(stack._items)					# Вывести эл-ты stack (напр. deque([]))
# print(list(stack._items))		# Вывести эл-ты stack в виде массива (напр. [])
# print(list(reversed(stack._items)))		# Вывести эл-ты stack в порядке LIFO (от последнего добавленного к первому)

def generate_start_matrix(rows=5, cols=5):
		"""Генерация начальной матрицы (лабиринта) заданной размерности"""
		matrix = np.full((rows, cols), '#', dtype=str)
		# i, j = np.indices((rows, cols))		# Создать сетку координат строк и столбцов
		# # Заменить нужные эл-ты на основе логической маски (Boolean indexing) -> '#'
		# matrix[(i % 2 == 0) | (j % 2 == 0)] = '#'		# Стены
		return matrix

# matrix = generate_start_matrix()
# print(matrix)
# start = (1, 1)
# print(matrix[start])		# == print(matrix[start[0], start[1]])
# print(matrix[start[0] + 1, start[1]])

"""
ПОДЗАДАЧИ:
	- Инициализация
	- Главный цикл
	- Удаление стен

КЛЮЧЕВОЕ: path (маршрут) - стек, visited (посещённые комнаты) - карта для всего лабиринта

ПСЕВДОКОД:
1. Инициализировать начальную матрицу (лабиринт)
2. Инициализировать посещённые комнаты (set)
3. Инициализировать маршрут (stack)
4. Инициализировать стартовую комнату (координата, tuple)
5. Добавить стартовую комнату в посещённые комнаты (set.add(start))
6. Добавить стартовую комнату в маршрут (stack.push(start))

7. ПОКА маршрут не пуст (not stack.is_empty)
    1. Достать из маршрута и очистить последнюю комнату (stack.pop()) -> текущая комната
    2. Определить координаты соседних комнат для текущей (array) -> все направления движения
		3. Определить валидные координаты соседних комнат (array) -> потенциальные направления движения
    4. ДЛЯ всех соседних комнат:
        1. ЕСЛИ соседняя комната лежит в диапазоне лабиринта И не посещённая
						1. Добавить соседнюю комнату в потенциальные направления движения
		5. ЕСЛИ существуют потенциальные направления
				1. Добавить текущую комнату в маршрут
				2. Выбрать случайную соседнюю комнату в качестве направления (random.choice)
				3. Удалить стену между текущей комнатой и выбранным соседом
				4. Добавить выбранного соседа в посещённые комнаты
				5. Добавить выбранного соседа в маршрут
		6. Иначе (потенциальные направления отсутствуют)
				1. Переходим к следующей итерации по маршруту (continue)
8. Завершить генерацию (return)
"""

def generate_maze(rows=5, cols=5):
		maze = generate_start_matrix(rows, cols)
		visited = set()
		path = Stack()

		start = (1, 1)
		visited.add(start)
		path.push(start)

		while not path.is_empty():
				room = path.pop()
				maze[room] = ' '		# Очистить комнату

				# nbs - neighbors (nb - neighbor)
				nbs = [(room[0] - 2, room[1]),
							 (room[0], room[1] - 2),
							 (room[0] + 2, room[1]),
							 (room[0], room[1] + 2)]
				# print(f"nbs: {nbs}")
				valid = []
				for nb in nbs:
						r, c = nb
						if ((0 < r < rows) and (0 < c < cols) and (nb not in visited)):
								valid.append(nb)
				# print(f"valid: {valid}")
				if valid:
					path.push(room)
					new_room = random.choice(valid)

					# Удалить стену между текущей комнатой и выбранным соседом
					wall = ((room[0] + new_room[0]) // 2, (room[1] + new_room[1]) // 2)
					maze[wall] = ' '

					visited.add(new_room)
					path.push(new_room)
				else:
					continue
				
		return maze

print(generate_maze(11, 11))