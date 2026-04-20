import time
import json
import platform

SIZE = 1_048_676_000 # 1024 * 1024 * 1000
STRIDE = 4096
PASSES = 1000

data = bytearray(SIZE)

start_time = time.time()

checksum = 0
for _ in range(PASSES):
    for i in range(0, SIZE, STRIDE):
        data[i] = (data[i] + 1) % 256
        checksum += data[i]

elapsed = time.time() - start_time

print(json.dumps({
    "benchmark": "memory",
    "hostname": platform.node(),
    "bytes_touched": SIZE * PASSES,
    "passes": PASSES,
    "checksum": checksum,
    "elapsed_seconds": round(elapsed, 2)
}))
