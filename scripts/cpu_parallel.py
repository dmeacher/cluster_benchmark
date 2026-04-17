import time
import json
import platform

start = time.time()
x = 0
for i in range(50_000_000):
    x += i % 7
end = time.time()

print(json.dumps({
    "benchmark": "cpu_parallel",
    "hostname": platform.node(),
    "time_seconds": round(end - start, 3),
    "checksum": x
}))
