# HTCondor Mini‑Cluster Benchmark Suite

This repository contains a lightweight benchmarking suite designed for
**small HTCondor clusters** used in instructional or experimental settings. It
is intended for use on clusters consisting of
**one head node and a small number of compute nodes** (e.g., 3 worker nodes),
each with modest hardware (older desktop PCs with ~8 GB RAM).

The benchmarks are written in **pure Python**, require no special libraries,
and are orchestrated using **HTCondor DAGMan**.

---

## Goals of This Benchmark

This benchmark suite is designed to:

- Compare **hardware performance** across similar but non‑identical nodes
- Observe **HTCondor scheduling behavior** on small clusters
- Measure **CPU, memory, and disk I/O performance**
- Provide repeatable, comparable results across student groups
- Reinforce best practices for HTC experimentation

Each benchmark is run **three times** to allow calculation of averages and
variability.

---

## Cluster Assumptions

This benchmark assumes:

- HTCondor is already installed and configured
- Python 3 is available on all execute nodes
- Each compute node has:
  - ~8 GB RAM
  - Local disk storage available for scratch files
- Jobs are allowed to run in the current working directory

No MPI, GPUs, or special kernel features are required.

---

## Repository Structure

```
.
├── scripts/
│   ├── cpu_single.py
│   ├── cpu_parallel.py
│   ├── memory_stress.py
│   └── io_test.py
│
├── benchmark.dag
├── cpu_single.submit
├── cpu_parallel.submit
├── memory.submit
├── io.submit
└── README.md
```

---

## Benchmarks Included

### 1. CPU Single‑Core Benchmark (`cpu_single.py`)
- Computes prime numbers up to a fixed limit
- Uses a single CPU core
- Measures raw single‑thread performance
- Useful for comparing different CPU generations

Each run produces a JSON‑formatted result with execution time.

---

### 2. CPU Throughput / Scheduler Stress (`cpu_parallel.py`)
- Integer arithmetic workload
- Multiple identical jobs submitted simultaneously
- Designed to exceed available slots
- Measures:
  - Queueing behavior
  - Fairness
  - Overall throughput

This benchmark highlights how HTCondor schedules jobs under load.

---

### 3. Memory Stress Benchmark (`memory_stress.py`)
- Allocates ~1.5–2 GB of memory
- Sequentially touches memory to force real allocation
- Safe for nodes with 8 GB RAM
- Reveals:
  - Memory bandwidth
  - Swapping or eviction issues
  - Node instability under load

---

### 4. Disk I/O Benchmark (`io_test.py`)
- Writes and deletes a 512 MB file
- Tests local disk performance
- Useful on older PCs where storage varies widely
- Highlights filesystem and disk differences

---

## Repeated Execution

Each benchmark is run **three times** using HTCondor’s `queue` mechanism.

Output files are uniquely named using the `$(Process)` macro, for example:

```
cpu_single_run0.out
cpu_single_run1.out
cpu_single_run2.out
```

This allows students to compute:
- Mean execution time
- Variability (standard deviation)
- Node‑to‑node differences

---

## Running the Benchmark Suite

From the directory containing the files:

```bash
condor_submit_dag benchmark.dag
```

You can monitor progress using:

```bash
condor_q
condor_job_queue_stats
```

After completion, output files will contain JSON‑formatted results.

---

## Interpreting Results

Each `.out` file contains structured output similar to:

```json
{
  "benchmark": "cpu_single",
  "hostname": "compute-node-1",
  "time_seconds": 2.341,
  "primes_found": 5133
}
```

Students are encouraged to:
- Aggregate results across runs
- Compare performance between nodes
- Identify scheduling effects
- Explain observed variance

---

## Suggested Student Analysis Questions

- Why do some runs take longer than others?
- How does node hardware affect performance?
- What happens when more jobs are queued than CPU slots?
- How consistent are memory and I/O measurements?
- Which benchmark shows the most variability, and why?

---

## Safety and Resource Considerations

- Memory usage is intentionally capped to avoid exhausting 8 GB nodes
- Disk I/O files are deleted automatically
- CPU workloads are finite and intentionally modest
- Jobs are non‑privileged and safe for shared instructional clusters

---

## Extending This Benchmark

Possible extensions include:
- Automated result aggregation scripts
- Plotting results with pandas/matplotlib
- Pinning jobs to specific nodes
- Varying `request_cpus` or memory limits
- Scaling to larger clusters

---

## License and Usage

This benchmark is intended for **educational use**. Instructors are
encouraged to modify and adapt it to their course needs.

---

If you have suggestions or improvements, feel free to fork and extend this suite.
