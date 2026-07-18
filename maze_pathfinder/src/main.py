from maze import generate_maze, print_maze
from search import bfs, visual_path


def main(rows=11, cols=11):
		print("\n=== Maze generation ===\n")
		maze, graph = generate_maze(rows, cols)
		print_maze(maze)

		# print("\n=== Maze graph ===\n")
		# graph.print_graph()

		print("\n=== Shortest path search (BFS) ===\n")
		shortest_path = bfs(graph, (1, 1), (rows - 2, cols - 2))
		# print(short_path)
		print_maze(visual_path(maze, shortest_path))


if __name__ == "__main__":
		main()