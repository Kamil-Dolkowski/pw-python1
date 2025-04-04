# Wątki w Pythonie nie wykonują się równolegle

# Proces - niezależny byt
# Wątek - część wspólnego procesu, współdzieli przestrzeń adresową z innymi wątkami

import multiprocessing
import time
import random

myList =[]

def job(n):
    myList.append(n)
    v = 0
    for i in range(1000):
        for j in range(1000):
            v += i*j
    print(f"Worker number {n}")
    print(len(myList))
    print(myList)

def test():
    workers = []

    begin = time.time()

    for i in range(24):
        worker = multiprocessing.Process(target=job, args=(i,))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

    end = time.time()

    print("Done")
    print(f"Working time {end-begin} s")

    print(len(myList))
    print(myList)

if __name__ == "__main__":
    test()