import pandas as pd
import numpy as np
from core.metrics import compute_conversion, compute_reaction_rate
from plotting import plot_conversion, plot_reaction_rate
from core.data_extractor import load_data

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
all_values = np.concatenate([conversion_base, 
                             conversion_fast, 
                             conversion_slow])
plot_conversion(time,
                np.max(all_values),
                [conversion_base, conversion_fast, conversion_slow],
                ["Base", "Fast Reaction", "Slow Reaction"])

plot_reaction_rate(time,
                   [compute_reaction_rate(CA_out, time),                
                    compute_reaction_rate(CA_out_fast, time), 
                    compute_reaction_rate(CA_out_slow, time)],
                   ["Base", "Fast Reaction", "Slow Reaction"])
