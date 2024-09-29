package main

import (
	"encoding/csv"
	"fmt"
	"os"
	"time"
)

// DynamicStruct grows in size based on the loop iteration
type DynamicStruct struct {
	data []byte
}

type LargeStruct struct {
	data [1024 * 1024 * 1024]byte // 1024MB of data (1 GB)
}

// PassByValue passes the struct by value
func PassByValue(ds DynamicStruct) DynamicStruct {
	return ds
}

// PassByPointer passes the struct by pointer
func PassByPointer(ds *DynamicStruct) *DynamicStruct {
	return ds
}

func benchmark(size int) (time.Duration, time.Duration) {
	// Create a struct of 'size' bytes
	ds := DynamicStruct{data: make([]byte, size)}

	// Measure time for pass by value
	start := time.Now()
	for i := 0; i < 1000; i++ {
		_ = PassByValue(ds)
	}
	durationValue := time.Since(start)

	// Measure time for pass by pointer
	start = time.Now()
	for i := 0; i < 1000; i++ {
		_ = PassByPointer(&ds)
	}
	durationPointer := time.Since(start)

	return durationValue, durationPointer
}

func main() {
	// Create a CSV file to store the data
	file, err := os.Create("benchmark_data.csv")
	if err != nil {
		fmt.Println("Error creating CSV file:", err)
		return
	}
	defer file.Close()

	writer := csv.NewWriter(file)
	defer writer.Flush()

	// Write CSV header
	writer.Write([]string{"Size(MB)", "PassByValue(ns)", "PassByPointer(ns)"})

	// Run benchmarks for sizes from 1 byte to 1024MB (1 Gb)
	for size := 1; size <= 1*1024*1024*1024; size *= 2 { // Increase size by 2x
		durationValue, durationPointer := benchmark(size)

		// Convert size to megabytes for easier readability
		sizeMB := float64(size) / (1024 * 1024)

		// Write the results to CSV (size in MB, passByValue time, passByPointer time)
		writer.Write([]string{
			fmt.Sprintf("%.8f", sizeMB),
			fmt.Sprintf("%d", durationValue.Nanoseconds()),
			fmt.Sprintf("%d", durationPointer.Nanoseconds()),
		})

		// Print status to monitor progress
		fmt.Printf("Completed benchmark for size: %.8f MB \n", sizeMB)
	}

	fmt.Println("Benchmark data exported to benchmark_data.csv")
}
