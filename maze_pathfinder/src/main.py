from maze import generate_maze, print_maze
from search import bfs


def main(rows=11, cols=11):
		print("\n=== Maze generation ===\n")
		maze, graph = generate_maze(rows, cols)
		print_maze(maze)

		print("\n=== Maze's graph ===\n")
		graph.print_graph()

		print("\n=== Shortest path search (BFS) ===\n")
		print(bfs(graph, (1, 1), (rows - 2, cols - 2)))


if __name__ == "__main__":
		main()