from maze import generate_maze, print_maze


def main(rows=11, cols=11):
		print("\n=== Maze generation ===\n")
		maze = generate_maze(rows, cols)
		print_maze(maze)
		
		print("\n=== Shortest path search (BFS) ===\n")
		pass

if __name__ == "__main__":
		main()