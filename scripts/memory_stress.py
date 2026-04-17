import time
import json
import platform

size = 200_000_000  # ~1.6GB of int8
start = time.time()

data = bytearray(size)
for i in range(0, size, 4096):
    data[i] = 1

checksum = sum(data[i] for i in range(0, size, 4096))
end = time.time()

print(json.dumps({
    "benchmark": "memory",
    "hostname": platform.node(),
    "time_seconds": round(end - start, 3),
    "checksum": checksum
}))
