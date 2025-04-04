# Wątki w Pythonie nie wykonują się równolegle

# Proces - niezależny byt
# Wątek - część wspólnego procesu, współdzieli przestrzeń adresową z innymi wątkami

import threading
import time
import random

myList =[]

def job(n):
    myList.append(n)
    print(f"Worker number {n}")

def test():
    workers = []

    begin = time.time()

    for i in range(24):
        worker = threading.Thread(target=job, args=(i,))
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