import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as anim


def create_grid(N: int):
    for x in range(N):
        row = []
        for y in range(N):
            row.append(random.randint(0, 1))
        grid.append(row)


def printgrid(grid):
    for i in grid:
        print(i)
    print("#" * 20)


def update(grid, N: int):
    new_grid = grid.copy()
    for x in range(N):
        for y in range(N):
            numcells = (
                # Upper row
                grid[(x - 1) % N][(y - 1) % N]
                + grid[x][(y - 1) % N]
                + grid[(x + 1) % N][(y - 1) % N]
                +
                # Middle row
                grid[(x - 1) % N][y]
                + grid[(x + 1) % N][y]
                +
                # Bottom row
                grid[(x - 1) % N][(y + 1) % N]
                + grid[x][(y + 1) % N]
                + grid[(x + 1) % N][(y + 1) % N]
            )

            state = grid[x][y]
            if state:
                if numcells < 2 or numcells > 3:
                    new_grid[x][y] = 0
            else:
                if numcells == 3:
                    new_grid[x][y] = 1


def main():
    N = 100
    update_interval = 50
    grid = create_grid(N)

    fig, ax = plt.subplots()
    img = ax.imshow(grid, interpolation="nearest")
    animation = anim.FuncAnimation(
        fig,
        update,
        fargs=(
            grid,
            N,
        ),
        frames=10,
        interval=update_interval,
    )

    plt.show()


main()
