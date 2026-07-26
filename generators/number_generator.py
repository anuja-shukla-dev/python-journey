n = int(input("Enter n: "))

def my_generator():
    for i in range(1,n+1):
        yield i

gen = my_generator()
for j in gen:
    print(j)