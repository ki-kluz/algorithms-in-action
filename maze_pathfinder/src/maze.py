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

# stack.push(10)
# print(list(stack._items))
# stack.push(20)
# print(list(stack._items))
# stack.push(30)
# print(list(stack._items))

# print(list(reversed(stack._items)))		# Вывести эл-ты stack в порядке LIFO (от последнего добавленного к первому)

def generate_start_matrix(rows=5, cols=5):
		"""Генерация начальной матрицы (лабиринта) заданной размерности"""
		matrix = np.full((rows, cols), '#', dtype=str)		# Создать пустую матрицу
		# i, j = np.indices((rows, cols))		# Создать сетку координат строк и столбцов
		# # Заменить нужные эл-ты на основе логической маски (Boolean indexing) -> '#'
		# matrix[(i % 2 == 0) | (j % 2 == 0)] = '#'		# Стены
		return matrix

# print(generate_start_matrix())

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
    1. Достать из маршрута последнюю комнату (stack.pop()) -> текущая комната
    2. Определить координаты соседних комнат для текущей (array) -> потенциальные направления движения
    3. ДЛЯ всех соседних комнат:
        1. ЕСЛИ соседняя комната НЕ лежит в диапазоне лабиринта ИЛИ посещённая
						1. Удалить соседнюю комнату из потенциальных направлений движения
		4. ЕСЛИ существуют потенциальные направлению
				1. Добавить текущую комнату в маршрут
				2. Выбрать случайную соседнюю комнату в качестве направления (random.choice)
				3. Удалить стену между текущей комнатой и выбранным соседом
				4. Добавить выбранного соседа в посещённые комнаты
				5. Добавить выбранного соседа в маршрут
		5. Иначе (потенциальные направления отсутствуют)
				1. Переходим к следующей итерации по маршруту (continue)
6. Завершить генерацию (return)
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
				# nbs - neighbors (nb - neighbor)
				nbs = [(room[0] - 2, room[1]),
							 (room[0], room[1] - 2),
							 (room[0] + 2, room[1]),
							 (room[0], room[1] + 2)]
				for nb in nbs:
						if ((nb[0] < 0 or nb[0] > rows) or \
								(nb[1] < 0 or nb[1] > cols) or \
								(nb in visited)):
								nbs.remove(nb)
				if nbs:
					path.push(room)
					new_room = random.choice(nbs)
					# Удалить стену между текущей комнатой и выбранным соседом
					visited.add(new_room)
					path.push(new_room)
				else:
					continue
				
		return maze

# print(generate_maze())