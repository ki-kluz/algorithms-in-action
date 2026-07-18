from structures import Graph, deque


def bfs(graph: Graph, start: tuple, finish: tuple):
		"""
		Поиск в ширину (BFS), через:
			- Двустороннюю очередь (deque)
			- Сохранение множества пройденных комнат
			- Ведение словаря родителей, для отслеживания: кто привёл в эту комнату?
		"""
		search_queue = deque()		# Создать очередь
		visited = set()		# Множество пройденных комнат
		parents = {}		# Словарь родителей

		visited.add(start)		# Добавить координату начала как пройденную
		parents[start] = None		# У координаты начала нет родителя (корень)
		search_queue.append(start)		# Добавить координату начала в очередь

		while search_queue:			# Пока очередь не пуста
				current = search_queue.popleft()		# Получить комнату (текущую)

				if current == finish:		# Если текущая равна финишной
						# Восстанавливаем кратчайший путь через родителей
						return reconstruct_path(parents, finish)
				
				for neighbor in graph.get_neighbors(current):		# Для всех соседей текущей комнаты
						if neighbor not in visited:			# Если сосед не посещён
								visited.add(neighbor)
								parents[neighbor] = current
								search_queue.append(neighbor)		# Добавить соседей для соседа
		return None		# Очередь пуста, а finish не найден - пути нет

def reconstruct_path(parents: dict, finish: tuple):
		"""Восстановить путь от finish до start через родителей"""
		path = []
		current = finish

		while current is not None:
				path.append(current)
				current = parents[current]
		# Путь собран от finish к start - переворачиваем
		return list(reversed(path))

def visual_path(maze, path, symbol: str='.'):
		"""Визуализация кратчайшего пути в лабиринте"""
		for r, c in path:
				maze[r, c] = symbol
		return maze