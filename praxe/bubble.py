from time import perf_counter
from random import uniform
import multiprocessing as mp


def bubble(array: list[float|int]):
    for end in range(len(array)-1, 0, -1):
        # last: int = 0
        for i in range(0, end):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        #         last = i
        # if not last:
        #     break
    return array
"""
def insertion(array: list[float|int], pipe=None) -> list[float | int]:
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    if not isinstance(pipe, type(None)):
        pipe.send(array)
    return array

def insertion(array: list[float|int], pipe=None) -> list[float | int]:
    for index, number in enumerate(array[1:], 1):
        while index > 0 and array[index-1] > number:
            array[index], array[index-1] = array[index-1], array[index]
            index -= 1
    if not isinstance(pipe, type(None)):
        pipe.send(array)
    return array
"""

def insertion(arr, pipe=None) -> list[float | int]:
     
    if (n := len(arr)) <= 1:
      return []
    for i in range(1, n):
         
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >=0 and key < arr[j] :
                arr[j+1] = arr[j]
                j -= 1
        arr[j+1] = key
    if not isinstance(pipe, type(None)):
        pipe.send(arr)
    
    return arr

"""count = 0
dump = 0
while True:
    array: list[float] = [uniform(-1000.0, 1000.0) for _ in range(10000)]
    ts = perf_counter()
    back = bubble(array)
    tn = perf_counter()
    count += 1
    dump += tn - ts
    assert back == sorted(array)
    print(f"\rsort: {dump/count} seconds", end="")"""

if __name__ == "__main__":
    jádra = mp.cpu_count()
    rozsah = jádra * 1000
    while True:
        array: list[float] = [uniform(-1000.0, 1000.0) for _ in range(rozsah)]
        ts = perf_counter()
        for i in range(jádra):
            globals()[f"pipe_p_{i}"], globals()[f"pipe_c_{i}"] = mp.Pipe()
            globals()[f"p{i}"] = mp.Process(target=insertion, args=( array[i::jádra], globals()[f"pipe_c_{i}"]))
            globals()[f"p{i}"].start()
        back1: list[list[float|int]] = []
        for i in range(jádra):
            back1.append(globals()[f"pipe_p_{i}"].recv())
        back: list[float | int] = insertion([back1[i][j] for j in range(rozsah//jádra) for i in range(jádra)])
        tn: float = perf_counter()
        assert back == sorted(array)
        print(f"\rsort: {tn-ts} seconds", end="")