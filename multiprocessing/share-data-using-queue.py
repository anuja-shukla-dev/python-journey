import multiprocessing
import time
import queue

def producer(q):
    for i in range(1, 11):
        print(f"Produced {i}", flush=True)
        q.put(i)
        time.sleep(0.5)
    q.put("DONE")


def consumer(q):
    print("Consumer started", flush=True)
    while True:
        item = q.get()

        if item == "DONE":
            break

        print(f"{item} printed", flush=True)


if __name__ == '__main__':
    q = multiprocessing.Queue()

    p1 = multiprocessing.Process(target=producer,args=(q,))
    p2 = multiprocessing.Process(target=consumer,args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()