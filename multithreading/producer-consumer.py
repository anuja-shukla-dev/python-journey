import threading
import time
import queue

q = queue.Queue()

def producer():
    for i in range(1,11):
        print(f"Produces {i}")
        q.put(i)
        time.sleep(0.5)

def consumer():
    while True:
        item = q.get()
        print(f"Consumed {item}")
        q.task_done()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer, daemon=True)


producer_thread.start()
consumer_thread.start()


producer_thread.join()

q.join()

print("All tasks completed")