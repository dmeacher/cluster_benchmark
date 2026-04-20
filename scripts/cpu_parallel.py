import time
import json
import platform

ITERATIONS = 1_000_000_000   # <<< calibrate once

start_time = time.time()

x = 0
for i in range(ITERATIONS):
    x += (i % 7) * (i % 13)

elapsed = time.time() - start_time

print(json.dumps({
    "benchmark": "cpu_parallel",
    "hostname": platform.node(),
    "iterations": ITERATIONS,
    "checksum": x,
    "elapsed_seconds": round(elapsed, 2)
}))
