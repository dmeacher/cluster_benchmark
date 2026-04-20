import time
import math
import json
import platform

def is_prime(n):
    if n < 2:
        return False
    r = int(math.sqrt(n)) + 1
    for i in range(2, r):
        if n % i == 0:
            return False
    return True

START = 2
END = 12_000_000

start_time = time.time()

count = 0
for n in range(START, END):
    if is_prime(n):
        count += 1

elapsed = time.time() - start_time

print(json.dumps({
    "benchmark": "cpu_single",
    "hostname": platform.node(),
    "numbers_tested": END - START,
    "primes_found": count,
    "elapsed_seconds": round(elapsed, 2)
}))
