from typing import List, Tuple
import heapq

# def a_star(
#     maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]
# ) -> Tuple[int, int]:
#     """
#     A* algorithm to find the shortest path from start to end on the given maze.

#     :param maze: List of lists representing the maze, where 0 is an empty space and 3 is a wall.
#     :param start: Tuple representing the starting position (row, col).
#     :param end: Tuple representing the ending position (row, col).
#     :return: Tuple representing the next position to move to (row, col).
#     """

#     # Define the heuristic function (Manhattan distance)
#     def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
#         return abs(a[0] - b[0]) + abs(a[1] - b[1])

#     # Initialize the open and closed sets
#     open_set = []
#     closed_set = set()

#     # Add the starting node to the open set
#     heapq.heappush(open_set, (0, start))
#     g_score = {start: 0}

#     while open_set:
#         # Get the node with the lowest f score from the open set
#         current = heapq.heappop(open_set)[1]

#         # Check if we've reached the end
#         if current == end:
#             return current

#         # Add the current node to the closed set
#         closed_set.add(current)

#         # Loop through the neighbors of the current node
#         for neighbor in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
#             # Get the neighbor's position
#             neighbor_pos = (current[0] + neighbor[0], current[1] + neighbor[1])

#             # Check if the neighbor is within the maze bounds and not a wall
#             if (
#                 0 <= neighbor_pos[0] < len(maze)
#                 and 0 <= neighbor_pos[1] < len(maze[0])
#                 and maze[neighbor_pos[0]][neighbor_pos[1]] != 3
#             ):
#                 # Calculate the tentative g score for the neighbor
#                 tentative_g_score = g_score[current] + 1

#                 # Check if we've already visited the neighbor
#                 if neighbor_pos in closed_set:
#                     if tentative_g_score >= g_score.get(neighbor_pos, float("inf")):
#                         continue

#                 # Check if we've found a new best path to the neighbor
#                 if tentative_g_score < g_score.get(neighbor_pos, float("inf")):
#                     # Update the g score and f score for the neighbor
#                     g_score[neighbor_pos] = tentative_g_score
#                     f_score = tentative_g_score + heuristic(neighbor_pos, end)

#                     # Add the neighbor to the open set
#                     heapq.heappush(open_set, (f_score, neighbor_pos))

#     # If we reach here, there is no path to the end
#     exit("No path found")

came_from = {}


def a_star(
    maze: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]
) -> Tuple[int, int]:
    """
    A* algorithm to find the shortest path from start to end on the given maze.

    :param maze: List of lists representing the maze, where 0 is an empty space and 3 is a wall.
    :param start: Tuple representing the starting position (row, col).
    :param end: Tuple representing the ending position (row, col).
    :return: Tuple representing the next position to move to (row, col).
    """

    # Define the heuristic function (Manhattan distance)
    def heuristic(a: Tuple[int, int], b: Tuple[int, int]) -> int:
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    # Initialize the open and closed sets
    open_set = []
    closed_set = set()

    # Add the starting node to the open set
    heapq.heappush(open_set, (0, start))
    g_score = {start: 0}

    while open_set:
        # Get the node with the lowest f score from the open set
        current = heapq.heappop(open_set)[1]

        # Check if we've reached the end
        if current == end:
            # Trace back the path from the end to the start to find the next position to move to
            path = [end]
            while path[-1] != start:
                parent = came_from[path[-1]]
                path.append(parent)
            return path[-2]

        # Add the current node to the closed set
        closed_set.add(current)

        # Loop through the neighbors of the current node
        for neighbor in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            # Get the neighbor's position
            neighbor_pos = (current[0] + neighbor[0], current[1] + neighbor[1])

            # Check if the neighbor is within the maze bounds and not a wall
            if (
                0 <= neighbor_pos[0] < len(maze)
                and 0 <= neighbor_pos[1] < len(maze[0])
                and maze[neighbor_pos[0]][neighbor_pos[1]] != 3
            ):
                # Calculate the tentative g score for the neighbor
                tentative_g_score = g_score[current] + 1

                # Check if we've already visited the neighbor
                if neighbor_pos in closed_set:
                    if tentative_g_score >= g_score.get(neighbor_pos, float("inf")):
                        continue

                # Check if we've found a new best path to the neighbor
                if tentative_g_score < g_score.get(neighbor_pos, float("inf")):
                    # Update the g score and f score for the neighbor
                    g_score[neighbor_pos] = tentative_g_score
                    f_score = tentative_g_score + heuristic(neighbor_pos, end)

                    # Add the neighbor to the open set
                    heapq.heappush(open_set, (f_score, neighbor_pos))

                    # Keep track of the parent of the neighbor for tracing the path back later
                    came_from[neighbor_pos] = current

    # If we reach here, there is no path to the end
    exit("No path found")


maze = [
    [0, 0, 0, 0, 0],
    [0, 3, 0, 3, 0],
    [0, 0, 0, 0, 0],
    [0, 3, 3, 3, 0],
    [0, 0, 0, 0, 0],
]
start = (0, 0)
end = (4, 4)
while True:
    start = a_star(maze, start, end)
    print(start)
    if start == end:
        break
