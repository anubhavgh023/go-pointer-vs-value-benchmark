import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the CSV data
data = pd.read_csv('../benchmark_data.csv')

# Prepare the data for animation
sizes = data['Size(MB)'].values
pass_by_value_times = data['PassByValue(ns)'].values
pass_by_pointer_times = data['PassByPointer(ns)'].values

# Create the figure and axes for the plot with dark background
fig, ax = plt.subplots(figsize=(10, 6), facecolor="#212121")
ax.set_facecolor("#212121")  # Set the axes background color

# Create lines
line1, = ax.plot([], [], label='Pass By Value', color='#fc584c', marker='o')
line2, = ax.plot([], [], label='Pass By Pointer', color='#9cd9ff', marker='x')

# Set limits and labels
ax.set_xlim(min(sizes), max(sizes) * 1.1)  # Set X-axis limits
ax.set_ylim(0, max(max(pass_by_value_times), max(pass_by_pointer_times)) * 1.1)  # Set Y-axis limits
ax.set_xscale('log')  # Log scale for x-axis
ax.set_xlabel('Size (MB)', color='white')  # Set x-label color
ax.set_ylabel('Time (Nanoseconds)', color='white')  # Set y-label color
ax.set_title('Performance: Pass By Value vs Pass By Pointer', color='white')  # Set title color

# Customize legend
ax.legend(facecolor='gray', edgecolor='black', fontsize=10)  # Add legend with a background

# Customize grid
ax.grid(True, color='gray', linestyle='--', alpha=0.5)  # Set grid color and transparency

# Change the color of the ticks
ax.tick_params(axis='both', colors='white')  # Change tick colors

# Initialize the lines for animation
def init():
    line1.set_data([], [])
    line2.set_data([], [])
    return line1, line2

# Update function for each frame
def update(frame):
    line1.set_data(sizes[:frame + 1], pass_by_value_times[:frame + 1])
    line2.set_data(sizes[:frame + 1], pass_by_pointer_times[:frame + 1])
    return line1, line2

# Create the animation
ani = FuncAnimation(fig, update, frames=len(sizes), init_func=init, blit=True, repeat=True, interval=500)

ani.save('bench-gif.gif',writer='pillow',fps=5)

# Show the animation
plt.show()
