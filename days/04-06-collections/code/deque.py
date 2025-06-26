# deque
from collections import deque
import random
import timeit

lst = list(range(10000000))
deq = deque(range(10000000))

def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

print("List time:", timeit.timeit(lambda: insert_and_delete(lst), number=10))
print("Deque time:", timeit.timeit(lambda: insert_and_delete(deq), number=10))

# list is slower than deque for insertions and deletions at both ends
# deque is optimized for fast fixed-time appends and pops from both ends