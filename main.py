import pandas as pd
import numpy as np
from metrics import compute_conversion
from plotting import plot_conversion
from data_extractor import load_data

#load data
time, CA_in, CA_out = load_data("data.csv")

#compute conversion, reactor performance
# baseline
conversion_base = compute_conversion(CA_in, CA_out)

# fast reaction scenario
CA_out_fast = CA_out * 0.8
conversion_fast = compute_conversion(CA_in, CA_out_fast)

# slow reaction scenario
CA_out_slow = CA_out * 1.2
conversion_slow = compute_conversion(CA_in, CA_out_slow)

#plot results
all_values = np.concatenate([conversion_base, conversion_fast, conversion_slow])
plot_conversion(time,
                np.max(all_values),
                [conversion_base, conversion_fast, conversion_slow],
                ["Base", "Fast Reaction", "Slow Reaction"])
