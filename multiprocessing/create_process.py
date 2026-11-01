import multiprocessing
import os

def process1():
    print("Process 1 PID",os.getpid())
    for i in range(1,6):
        print(i)

def process2():
    print("Process 2 PID",os.getpid())
    for i in "ABCDE":
        print(i)

if __name__ == '__main__':
    p1 = multiprocessing.Process(name="Number process",target=process1)
    p2 = multiprocessing.Process(name="Letter process",target=process2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print("Main process finished")