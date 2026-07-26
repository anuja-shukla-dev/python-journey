from functools import lru_cache

@lru_cache(maxsize=None)
def ways(n):
    if n ==0:
        return 1
    if n == 1:
        return 1
    
    return ways(n-1)+ways(n-2)

print("Jumps:",ways(5))