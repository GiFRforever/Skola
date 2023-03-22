import requests
from time import sleep
from typing import List, Tuple
import heapq

url = "http://127.0.0.1:44822"

response = requests.get(url + "/init")
data = response.json()
bot_id = data["bot_id"]
# bot_id = "118430890877055178219468729343194839785"
print(bot_id)
input("Press enter to continue...")
response = requests.get(f"{url}/game/{bot_id}")
game_data = response.json()
# print(game_data)
game_info = game_data["game_info"]
map_resolutions = tuple(game_info["map_resolutions"].values())

game_map_raw = game_data["map"]
game_map = [[] for _ in range(map_resolutions[0])]
start_node = (0, 0)
goal_node = (0, 0)
orientation = 0
battery_mode = False
battery = 0
for ir, row in enumerate(game_map_raw):
    for ic, cell in enumerate(row):
        if cell["field"] in [2, 4] and "your_bot" in cell:
            start_node = (ir, ic)
            orientation = cell["orientation"]
            if "battery_level" in cell:
                # print("Battery:", cell["battery"])
                battery_mode = True
                battery = cell["battery_level"]
        elif cell["field"] == 1:
            goal_node = (ir, ic)
        game_map[ir].append(cell["field"])
# input("Press enter to continue...")
# print(game_map)
print("Start:", start_node)
print("Goal:", goal_node)


def pohni_se(odkud, kam) -> tuple[int, tuple[int, int]]:
    delta: tuple[int, int] = (kam[0] - odkud[0], kam[1] - odkud[1])
    match delta:
        case (-1, 0):
            print("nahoru")
            return (0, kam)
        case (0, 1):
            print("vpravo")
            return (1, kam)
        case (1, 0):
            print("dolů")
            return (2, kam)
        case (0, -1):
            print("vlevo")
            return (3, kam)
        case _:
            print("Delta:", delta)
            raise ValueError("Nepodporovany smer pohybu")


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


def check_battery() -> None:
    global battery
    global battery_mode
    while battery_mode:
        response = requests.get(f"{url}/game/{bot_id}")
        game_data = response.json()
        game_map_raw = game_data["map"]
        for row in game_map_raw:
            for cell in row:
                if cell["field"] in [2, 4] and "your_bot" in cell:
                    if "battery_level" in cell:
                        battery = cell["battery_level"]
        if battery < 1:
            while (
                requests.post(
                    f"{url}/action", data={"bot_id": bot_id, "action": "wait"}
                )
                == 200
            ):
                sleep(0.2)
            print("\nNabíjím...")
        else:
            break


current_node: tuple = start_node
while True:
    print("\nCurrent:", current_node)
    node = a_star(game_map, current_node, goal_node)
    print("Kam:", node)
    check_battery()
    směr, current_node = pohni_se(current_node, node)
    while směr != orientation:  # otáčení
        if směr == (orientation + 1) % 4:
            while (
                response := requests.post(
                    f"{url}/action", data={"bot_id": bot_id, "action": "turn_right"}
                )
            ) == 200:
                sleep(0.2)
            orientation = (orientation + 1) % 4
        else:
            while (
                response := requests.post(
                    f"{url}/action", data={"bot_id": bot_id, "action": "turn_left"}
                )
            ) == 200:
                sleep(0.2)
            orientation = (orientation - 1) % 4
    while (
        requests.post(f"{url}/action", data={"bot_id": bot_id, "action": "step"})
        == 200  # pohyb
    ):
        check_battery()
        sleep(0.2)
    if current_node == goal_node:
        exit("Konec hry")
    sleep(0.2)
