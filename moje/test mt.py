import multiprocessing as mp
from multiprocessing.connection import wait
def f(conn):
    while bu := conn.recv() is not None:
        bu = conn.recv()
        print(bu)
        print("received")
        conn.send("OK")

if __name__ == '__main__':
    jádra = mp.cpu_count()
    #parent_conn, child_conn = mp.Pipe()
    for i in range(jádra):
        globals()[f"pipe_p_{i}"], globals()[f"pipe_c_{i}"] = mp.Pipe()
        globals()[f"p{i}"] = mp.Process(target=f, args=(globals()[f"pipe_c_{i}"],))
        globals()[f"p{i}"].start()
    
    for i in range(jádra):
        globals()[f"pipe_p_{i}"].send(1) # spustí while loop
        globals()[f"pipe_p_{i}"].send("OK?")

    for i in range(jádra):
        print(globals()[f"pipe_p_{i}"].recv())   # prints "[42, None, 'hello']"
    
    for i in range(jádra):
        globals()[f"pipe_p_{i}"].send("next")

    for i in range(jádra):
        print(globals()[f"pipe_p_{i}"].recv())
    
    for i in range(jádra):
        globals()[f"p{i}"].join()
    exit()
