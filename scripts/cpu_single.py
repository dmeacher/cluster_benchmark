import time
import math
import json
import platform

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

start = time.time()
count = 0
limit = 50000

for i in range(limit):
    if is_prime(i):
        count += 1

end = time.time()

result = {
    "benchmark": "cpu_single",
    "hostname": platform.node(),
    "primes_found": count,
    "time_seconds": round(end - start, 3)
}

print(json.dumps(result, indent=2))
