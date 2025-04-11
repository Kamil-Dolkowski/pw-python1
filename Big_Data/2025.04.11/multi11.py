import multiprocessing
from multiprocessing import Lock
import time

def job(n, lock):
    print(f"Worker number {n}: begin")

    if n == 4:
        print(f"Worker number {n}: wait on lock")
        lock.acquire()
        time.sleep(10)
        lock.release()
    else:
        time.sleep(1)
        print(f"Worker number {n}: wait on lock")
        lock.acquire()
        pass
        lock.release()

    print(f"Worker number {n}: end")

def test():
    lock = Lock()
    workers = []

    for i in range(24):
        worker = multiprocessing.Process(target=job, args=(i, lock))
        workers.append(worker)
        worker.start()

    for worker in workers:
        worker.join()

    print("!!! DONE !!!")

if __name__ == "__main__":
    test()