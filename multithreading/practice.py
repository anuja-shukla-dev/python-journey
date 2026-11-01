import threading
import queue
import time

q = queue.Queue()

def producer():
    for i in range(1,6):
        print(f"Produced {i}")
        q.put(i)
        time.sleep(0.5)

    q.put(None)

def consumer():
    while True:
        item = q.get()

        if item is None:
            break

        print(f"{item} printed")
        q.task_done()

thread1 = threading.Thread(target=producer())
thread2 = threading.Thread(target=consumer())

thread1.start()
thread2.start()

thread1.join()
thread2.join()
print("Completed")