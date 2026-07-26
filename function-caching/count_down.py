from functools import lru_cache

@lru_cache(maxsize=None)
def count_down(n):
    if n==0:
        return
    
    print(n)
    count_down(n-1)

count_down(5)
count_down(5)