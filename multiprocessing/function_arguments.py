import multiprocessing

def calculate_square(number):
    print(f"Sqaure of {number}: {number*number}")

if __name__ == '__main__':
    numbers = [2,4,6,8,10]
    processes = []
    for num in numbers:
        p = multiprocessing.Process(target=calculate_square,args=(num,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
