import pandas as pd
import numpy as np
from tqdm import tqdm
from signal_processing import load_all as signal
import matplotlib.pyplot as plt

from util import *
from settings import *

# Extract data from gz files
full_strike_data = extract_all_gz(GZ_DIR)

# Save signals across all strikes
pnl_dict = signal(full_strike_data)

# Transform signals to lists for plotting
x_axis = [gz[5:8] for gz in pnl_dict.keys()]
y_axis = [
    sum(pnl_dict[gz][key][0] ** 2 for key in pnl_dict[gz].keys())
    for gz in pnl_dict.keys()
]

# Create a DataFrame for plotting
plot_df = pd.DataFrame({"x": x_axis, "y": y_axis}).sort_values(by="x")

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(plot_df.x, plot_df.y, marker="o", linestyle="-", color="b")
plt.xlabel("Strike (x-axis)")
plt.ylabel("Sum of PnL Squared (y-axis)")
plt.title("PnL Signals Across Strikes")
plt.grid(True)
plt.show()