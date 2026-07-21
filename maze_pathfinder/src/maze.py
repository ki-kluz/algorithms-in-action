import random

import numpy as np
from structures import Graph, Stack

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

def validate_size(rows, cols):
		"""Проверить, что размеры нечётные и >= 3"""
		if rows < 3 or cols < 3:
				raise ValueError(f"Размеры должны быть >= 3, получено: {rows}×{cols}")
		if rows % 2 == 0 or cols % 2 == 0:
				raise ValueError(f"Размеры должны быть нечётными, получено {rows}×{cols}")

def create_matrix(rows=11, cols=11):
		"""Генерация начальной матрицы (лабиринта) заданной размерности"""
		matrix = np.full((rows, cols), '#', dtype=str)
		return matrix

def get_neighbors(room, rows, cols, visited):
		"""Вернуть список валидных не посещённых соседних комнат"""
		neighbors = [(room[0] - 2, room[1]),
					 			 (room[0], room[1] - 2),
					 			 (room[0] + 2, room[1]),
					 			 (room[0], room[1] + 2)]
		# print(f"neighbors: {neighbors}")
		valid = []
		for neighbor in neighbors:
				r, c = neighbor
				if ((0 < r < rows) and (0 < c < cols) and (neighbor not in visited)):
						valid.append(neighbor)
		# print(f"valid: {valid}")
		return valid

def carve_passage(grid, room1, room2):
    """Удалить стену между первой и второй комнатой"""
    wall = ((room1[0] + room2[0]) // 2, (room1[1] + room2[1]) // 2)
    grid[wall] = ' '

def print_maze(maze):
		"""Вывод лабиринта"""
		for row in maze:
				print(*(row))


"""
РЕЗЮМЕ:
Идея провалилась, тк при дополнительном удалении стен нужно вести graph, иначе происходит только видоизменение картинки без влияния на работу...
Идея вероятности цикла (loop_prob):
 - ведения дополнительного построения "проходов" на этапе изначальной генерации графа
ВЫХОДИТ ЗА РАМКИ КУРСА (и проекта)
"""
# def randomize_passages(maze, visited: set, count: int=6):
# 		"""Удаление случайных стен и создание дополнительных проходов"""
# 		# Определение всех возможных стен
# 		walls = []
# 		for r in range(1, len(maze) - 1):
# 				for c in range(1, len(maze[r]) - 1):
# 						if (r, c) not in visited:
# 								walls.append((r, c))
# 		# Случайный выбор стен для удаления
# 		choice = random.sample(walls, count)
# 		# Удаление стен
# 		for r, c in choice:
# 				maze[r][c] = ' '
# 		return None


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

def generate_maze(rows=11, cols=11):
		"""Генерация лабиринта методом DFS (with backtracking)"""
		validate_size(rows, cols)

		maze = create_matrix(rows, cols)
		graph = Graph()
		visited = set()
		path = Stack()

		# Координаты начальной / конечной точки
		start, finish = (1, 0), (rows - 2, cols - 1)
		maze[start], maze[finish] = 'S', 'F'

		# Начинаем с первой комнаты (правее начальной точки)
		first_room = (start[0], start[1] + 1)
		graph.add_node(first_room)
		visited.add(first_room)
		path.push(first_room)

		while not path.is_empty():
				room = path.pop()
				maze[room] = ' '		# Очистить комнату

				valid = get_neighbors(room, rows, cols, visited)
				if valid:
					path.push(room)
					new_room = random.choice(valid)
					
					# Удалить стену между текущей комнатой и выбранным соседом
					carve_passage(maze, room, new_room)

					graph.add_edge(room, new_room, weight=1)
					visited.add(new_room)
					path.push(new_room)
				else:
					continue
		
		return maze, graph