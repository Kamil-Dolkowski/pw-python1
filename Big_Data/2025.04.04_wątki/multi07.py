# Kolejka

import multiprocessing
import time
from multiprocessing import Queue

def job(n, queue):
    queue.put(n)
    v = 0
    for i in range(1000):
        for j in range(1000):
            v += i*j
    print(f"Worker number {n}")

def test():
    queue = Queue()
    workers = []

    begin = time.time()

    for i in range(24):
        worker = multiprocessing.Process(target=job, args=(i,queue))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

    myList = []

    while not queue.empty():
        myList.append(queue.get())

    end = time.time()

    print("Done")
    print(f"Working time {end-begin} s")

    print(len(myList))
    print(myList)

if __name__ == "__main__":
    test()