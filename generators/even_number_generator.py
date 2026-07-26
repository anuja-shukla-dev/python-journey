start = 1
end = int(input("Enter end: "))

def even_num():
    for i in range(start,end+1):
        if i%2==0:
            yield i

num = even_num()
for n in num:
    print(n)