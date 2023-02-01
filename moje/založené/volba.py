import numpy as np
import multiprocessing as mp
from time import time

# import matplotlib.pyplot as plt
# import matplotlib

# matplotlib.use("TkAgg")

kolik_kandidátů = 10
kolik_voličů = 10_000
kolik_postupujicích = 2
iterací = 1000


def main(cislo_procesu: int, počítadlo, conn) -> None:
    # Create an array of shape (100, 10) filled with the integers 0 to 9
    arr = np.array([np.arange(kolik_kandidátů) for _ in range(kolik_voličů)])

    # Shuffle the elements of each row
    for i in range(arr.shape[0]):
        np.random.shuffle(arr[i])

    counts = np.zeros((kolik_kandidátů, kolik_kandidátů))
    for i in range(kolik_kandidátů):
        counts[:, i] = np.bincount(arr[:, i], minlength=kolik_kandidátů)

    # for j in range(counts.shape[1]):
    # print(" 0  1  2  3  4  5  6  7  8  9")
    # for j in range(1):
    #     for i in range(counts.shape[0]):
    #         print(f"{str(int(counts[i, j])):>2}", end=" ")
    # print()

    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection="3d")

    # x = np.arange(counts.shape[0])
    # y = np.arange(counts.shape[1])
    # x, y = np.meshgrid(x, y)

    # ax.bar3d(x.ravel(), y.ravel(), np.zeros(x.shape).ravel(), 1, 1, counts.ravel())

    # ax.set_xlabel("Column")
    # ax.set_ylabel("Number")
    # ax.set_zlabel("Count")

    # plt.show()

    # Find the indices of the 3 most common numbers in column 0
    most_common_values = np.argsort(-counts[:, 0])[:kolik_postupujicích]

    # print(most_common_values)

    # result = np.array([np.where(row == num)[0][0] for row in arr for num in most_common_values])
    # counts = np.bincount(result)

    # print(result)
    # print(counts)

    counts2 = np.zeros(len(most_common_values))
    for i in range(arr.shape[0]):
        for j in range(arr.shape[1]):
            if arr[i, j] in most_common_values:
                counts2[np.where(most_common_values == arr[i, j])] += 1
                break

    # print(counts2)

    with open("moje/volba.txt", "a") as f:
        f.write(", ".join([str(int(i)) for i in counts2]) + "\n")

    # print(počítadlo, end="\r")
    conn.send(počítadlo * cislo_procesu)


if __name__ == "__main__":
    jádra: int = mp.cpu_count()

    start: float = time()
    for počítadlo in range(iterací // jádra):
        it_t: float = time()
        for i in range(jádra):
            globals()[f"pipe_p_{i}"], globals()[f"pipe_c_{i}"] = mp.Pipe()
            globals()[f"prcs{i}"] = mp.Process(
                target=main, args=(i, počítadlo, globals()[f"pipe_c_{i}"])
            )
            globals()[f"prcs{i}"].start()
        for i in range(jádra):
            print(globals()[f"pipe_p_{i}"].recv(), f"{time()-it_t} s", end="\r")

    print(f"Time: {time() - start}")
    with open("moje/volba.txt", "r") as f:
        lines: list[str] = f.readlines()
        kand: list[int] = [0] * (lines[0].count(",") + 1)
        for line in lines:
            line = [int(float(x)) for x in line.split(", ")]
            kand[line.index(max(line))] += 1
        print(kand)
        print(*[f"{round((100 * x)/sum(kand), 2)}%" for x in kand])
