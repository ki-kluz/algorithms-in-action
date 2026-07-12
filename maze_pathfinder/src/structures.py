from collections import deque


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


class Graph:
		def __init__(self):
				"""Создание структуры данных: граф"""
				self.graph = {}
		
		def add_node(self, node: tuple):
				"""Добавление нового узла в граф"""
				if node not in self.graph:
						self.graph[node] = {}
						
		def add_edge(self, node1: tuple, node2: tuple, weight: int):
				"""Добавление ребра(связи) в граф"""
				# Добавить новые узлы (если отсутствуют)
				self.add_node(node1)
				self.add_node(node2)
				# Делаем связь двунаправленной
				self.graph[node1][node2] = weight
				self.graph[node2][node1] = weight

		def get_neighbors(self, node: tuple):
				"""Возвращение соседей и веса рёбер для узла"""
				return self.graph.get(node, {})

		def print_graph(self):
				"""Вывод данных графа (узлы/ребра)"""
				for node in self.graph:
						print(f"{node}: {self.graph[node]}")
        
# graph = Graph()

# graph.add_node('A')
# graph.add_node('B')
# graph.add_node('C')

# graph.add_edge('A', 'B', 1)
# graph.add_edge('A', 'C', 3)

# print(graph.get_neighbors('A'))

# graph.print_graph()