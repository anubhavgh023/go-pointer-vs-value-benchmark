import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
data = pd.read_csv('../benchmark_data.csv')

# Plot the data
plt.figure(figsize=(10, 6))

plt.plot(data['Size(MB)'], data['PassByValue(ns)'], label='Pass By Value', marker='o')
plt.plot(data['Size(MB)'], data['PassByPointer(ns)'], label='Pass By Pointer', marker='x')

# Label the chart
plt.title('Performance: Pass By Value vs Pass By Pointer')
plt.xlabel('Size (MB)')
plt.ylabel('Time (Nanoseconds)')
plt.xscale('log')  # Log scale for better visualization of size progression
plt.legend()

# Show the plot
plt.grid(True)
plt.show()