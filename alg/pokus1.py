import requests
from time import sleep


def heuristic_cost(current_cell, goal_cell):
    return abs(current_cell[1] - goal_cell[1]) + abs(current_cell[0] - goal_cell[0])


def get_neighbors(current_cell, game_map):
    neighbors = []
    x, y = current_cell[1], current_cell[0]
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        new_x, new_y = x + dx, y + dy
        if (
            0 <= new_x < len(game_map)
            and 0 <= new_y < len(game_map[0])
            and game_map[new_x][new_y] != 3
        ):
            neighbors.append((new_y, new_x))
    return neighbors


def a_star(start_cell, goal_cell, game_map):
    open_set = [start_cell]
    closed_set = []
    g_score = {start_cell: 0}
    f_score = {start_cell: heuristic_cost(start_cell, goal_cell)}
    while open_set:
        current_cell = min(open_set, key=lambda x: f_score[x])
        if current_cell == goal_cell:
            path = []
            while current_cell in g_score:
                path.append(current_cell)
                current_cell = g_score[current_cell]
            path.reverse()
            return path
        open_set.remove(current_cell)
        closed_set.append(current_cell)
        for neighbor in get_neighbors(current_cell, game_map):
            if neighbor in closed_set:
                continue
            tentative_g_score = g_score[current_cell] + 1
            if neighbor not in open_set:
                open_set.append(neighbor)
            elif tentative_g_score >= g_score.get(neighbor, float("inf")):
                continue
            g_score[neighbor] = tentative_g_score
            f_score[neighbor] = tentative_g_score + heuristic_cost(neighbor, goal_cell)


url = "http://127.0.0.1:44822"

# response = requests.get(url + "/init")
# data = response.json()
# bot_id = data["bot_id"]
bot_id = "118430890877055178219468729343194839785"
print(bot_id)
# input("Press enter to continue...")
response = requests.get(f"{url}/game/{bot_id}")
game_data = response.json()
print(game_data)
game_info = game_data["game_info"]
map_resolutions = tuple(game_info["map_resolutions"].values())

game_map_raw = game_data["map"]
game_map = [[] for _ in range(map_resolutions[0])]
start_node = (0, 0)
goal_node = (0, 0)
orientation = 0
for ir, row in enumerate(game_map_raw):
    for ic, cell in enumerate(row):
        if cell["field"] == 2 and "your_bot" in cell:
            start_node = (ir, ic)
            orientation = cell["orientation"]
        elif cell["field"] == 1:
            goal_node = (ir, ic)
        game_map[ir].append(cell["field"])

print(game_map)
print(start_node)
print(goal_node)


def pohni_se(odkud, kam) -> tuple[int, tuple[int, int]]:
    delta: tuple[int, int] = (kam[0] - odkud[0], kam[1] - odkud[1])
    match delta:
        case (1, 0):
            print("nahoru")
            return (0, (odkud[0] - 1, odkud[1]))
        case (0, 1):
            print("vpravo")
            return (1, (odkud[0], odkud[1] + 1))
        case (-1, 0):
            print("dolů")
            return (2, (odkud[0] + 1, odkud[1]))
        case (0, -1):
            print("vlevo")
            return (3, (odkud[0], odkud[1] - 1))
        case _:
            print(delta)
            raise ValueError("Nepodporovany smer pohybu")


while True:
    current_node: tuple = start_node
    path = a_star(current_node, goal_node, game_map)
    print(path)
    if path:
        print("Path found:")
        for node in path:
            node = (node[1], node[0])
            print(node)
            směr, current_node = pohni_se(start_node, node)
            while směr != orientation:
                response = requests.post(
                    f"{url}/action", data={"bot_id": bot_id, "action": "turn_right"}
                )
                print(response.json())
                orientation = (orientation + 1) % 4
                sleep(2)
            response = requests.post(
                f"{url}/action", data={"bot_id": bot_id, "action": "step"}
            )
            print(response.json())
            sleep(2)
    else:
        print("No path found")
