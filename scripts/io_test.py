import time
import os
import json
import platform

FILE_SIZE_MB = 1024
ITERATIONS = 100

block = b"x" * (1024 * 1024)
filename = "iotest.dat"

start_time = time.time()

for _ in range(ITERATIONS):
    with open(filename, "wb") as f:
        for _ in range(FILE_SIZE_MB):
            f.write(block)

    with open(filename, "rb") as f:
        while f.read(1024 * 1024):
            pass

    os.remove(filename)

elapsed = time.time() - start_time

print(json.dumps({
    "benchmark": "io",
    "hostname": platform.node(),
    "iterations": ITERATIONS,
    "file_size_mb": FILE_SIZE_MB,
    "total_mb_written": ITERATIONS * FILE_SIZE_MB,
    "elapsed_seconds": round(elapsed, 2)
}))
