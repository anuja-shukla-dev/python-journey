import threading

def printNumbers():
    for i in range(1,6):
        print(i)

def printLetters():
    for i in "ABCDE":
        print(i)

thread1 = threading.Thread(target= printNumbers())
thread2 = threading.Thread(target= printLetters())

thread1.start()
thread2.start()

thread1.join()
thread2.join()