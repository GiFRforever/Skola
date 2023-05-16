from time import sleep


class Table:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.table: list[list[int]] = [[0 for i in range(x)] for j in range(y)]

    def rules(self, x, y):
        if self.table[x][y] == 1:
            if (n := self.neighbors(x, y)) < 2:
                return 0
            elif n > 3:
                return 0
            else:
                return 1
        else:
            if self.neighbors(x, y) == 3:
                return 1
            else:
                return 0

    def neighbors(self, x, y) -> int:
        _neighbors: int = 0
        for x_alt in range(x - 1, x + 2):
            for y_alt in range(y - 1, y + 2):
                if x_alt == x and y_alt == y:
                    continue
                elif x_alt < 0 or x_alt >= self.x:
                    continue
                elif y_alt < 0 or y_alt >= self.y:
                    continue
                else:
                    _neighbors += self.table[y][x]
        return _neighbors

    def cycle(self) -> None:
        new_table: list[list[int]] = self.table.copy()
        for x in range(self.x):
            for y in range(self.y):
                new_table[y][x] = self.rules(x, y)
        self.table = new_table.copy()

    def render(self):
        for y in self.table:
            for x in y:
                print("\33[106mU+025A0")

    def commence(self):
        while True:
            self.cycle()
            sleep(0.1)


size_x: int = 100
size_y: int = 100
game_of_death: Table = Table(size_x, size_y)
