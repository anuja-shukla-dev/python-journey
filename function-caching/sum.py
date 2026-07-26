from functools import lru_cache

@lru_cache(maxsize=None)
def total(n):
    if n==0:
        return 0
    
    return n+total(n-1)

print("Sum:",total(5))

