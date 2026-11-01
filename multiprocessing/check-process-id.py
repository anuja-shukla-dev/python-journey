import multiprocessing
import os

def childProcess():
    print("Child PID",os.getpid())
    print("Parent PID",os.getppid())

if __name__ == '__main__':
    print("Main PID",os.getpid())
    p1 = multiprocessing.Process(target=childProcess)

    p1.start()
    p1.join()

