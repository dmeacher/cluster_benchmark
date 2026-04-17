import time
import os
import json
import platform

filename = "iotest.dat"
size_mb = 512
block = b"x" * (1024 * 1024)

start = time.time()
with open(filename, "wb") as f:
    for _ in range(size_mb):
        f.write(block)
end = time.time()

os.remove(filename)

print(json.dumps({
    "benchmark": "io",
    "hostname": platform.node(),
    "mb_written": size_mb,
    "time_seconds": round(end - start, 3)
}))
