
# Pass by Value vs. Pass by Pointer Benchmark in Go

This project benchmarks the performance difference between **pass by value** and **pass by pointer** when dealing with structs in Go, focusing on large data structures. The benchmark shows how performance varies as the size of the struct increases.

## Overview

When passing a struct to a function in Go, you can either:

1. **Pass by Value**: This creates a copy of the struct, which consumes more memory and time as the size of the struct increases.
2. **Pass by Pointer**: This passes the memory address of the struct, which avoids copying and is typically faster for larger structs.

### What this project demonstrates

- The performance difference between passing large structs by value vs. by pointer.
- The project measures execution time for struct sizes starting from 1MB up to 1GB.
- The results are saved in a CSV file and visualized using Python.

## Project Structure

```bash
go-pointer-vs-value-benchmark/
    ├── py-graph/           # Python visualization and animation
    │   ├── venv/           # Python virtual environment (optional)
    │   ├── animate.py      # Python script for animated graph visualization
    │   ├── visualize.py    # Python script for static visualization
    │   ├── bench-gif.gif   # Example animated graph of the benchmark
    ├── benchmark_data.csv  # Output CSV file with benchmark results
    ├── go.mod              # Go module file
    ├── go.sum              # Go dependencies file
    ├── main.go             # Go code to run benchmarks
    ├── PassByValue-vs-PassByPointer.img  # Sample image showing graph
```

## Requirements

### Go

You need Go 1.23.1 or later installed. If Go is not installed, follow the instructions on [Go's official website](https://golang.org/doc/install).

### Python (for visualization)

- Python 3.8 or higher
- Install required Python libraries via `requirements.txt` (optional)
  
    ```bash
    pip install -r requirements.txt
    ```

## Setup and Running the Benchmark

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/learning-do.git
    cd learning-do
    ```

2. **Run the benchmark**

    The `main.go` file runs a benchmark for struct sizes from 1MB to 1GB, measuring the time taken for pass by value vs pass by pointer.

    ```bash
    go run main.go
    ```

    This will generate a CSV file `benchmark_data.csv` that contains the benchmark results.

    **Sample Output:**

    ```
    Size(MB), PassByValue(ns), PassByPointer(ns)
    1.00000000, 50000, 32000
    2.00000000, 110000, 70000
    ...
    ```

3. **Visualize the Results**

    After running the Go benchmark, you can visualize the results using the Python scripts provided.

    - **Static Plot:**

        ```bash
        cd py-graph
        python3 visualize.py
        ```

        This will generate a static plot comparing the performance of passing by value and by pointer.

    - **Animated Plot:**

        ```bash
        cd py-graph
        python animate.py
        ```

        This will generate an animated GIF that shows how performance changes as the struct size increases.

    - The animated GIF will be saved as `bench-gif.gif`.

## Project Files Explained

### Go Code (`main.go`)

The main Go file performs the benchmarking by creating structs of increasing sizes, from 1 byte to 1GB, and measures the time it takes to pass them by value vs. by pointer. 

**Key functions:**

- `PassByValue`: Passes the struct by value (copies the struct).
- `PassByPointer`: Passes the struct by pointer (no copying, only pointer passing).
- `benchmark`: Runs both methods for a specific struct size and returns the time taken for each.

### Python Scripts

1. `visualize.py`: A Python script using `matplotlib` to generate a static line graph of the benchmark results.
   
2. `animate.py`: A Python script using `matplotlib.animation` to generate an animated graph visualizing the benchmark results over time.

## Results

Based on this benchmark:

- **Pass by Value** is faster for very small struct sizes.
- **Pass by Pointer** performs significantly better for larger structs (typically noticeable at 10MB and beyond), as it avoids copying large amounts of memory.

## Example Visualization

![Pass by Value vs Pass by Pointer](../go-pointer-vs-value-benchmark/PassByValue(ns)andPassByPointer(ns).png)

## System Specifications

All benchmarks were performed on:

- **OS**: Pop!_OS 22.04 LTS
- **Processor**: Intel i5-1340P (13th Gen)
- **RAM**: 16 GB
- **GPU**: Intel Device a7a0

## License

This project is open source under the MIT License. Feel free to use and modify.
