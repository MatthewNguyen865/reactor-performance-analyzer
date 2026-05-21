import pandas as pd
import numpy as np
from core.metrics import compute_conversion, compute_reaction_rate
from plotting import plot_conversion, plot_reaction_rate
from core.data_extractor import load_data
from data_generator import generate_dataset

#generate and load data
#Note: plots in README.md use seed = 1
generate = input("Generate new dataset? (y/n): ")
if generate.lower() == "y":
    seed = input("Enter random seed (integer) or leave blank: ")
    if seed == "":
        seed = None
    else:
        seed = int(seed)
    generate_dataset(seed=seed)

time, CA_in, CA_out_base, CA_out_fast, CA_out_slow = load_data("data.csv")

#compute conversion, reactor performance
# baseline
conversion_base = compute_conversion(CA_in, CA_out_base)

# fast reaction scenario
conversion_fast = compute_conversion(CA_in, CA_out_fast)

# slow reaction scenario
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
                   [compute_reaction_rate(CA_out_base, time),                
                    compute_reaction_rate(CA_out_fast, time), 
                    compute_reaction_rate(CA_out_slow, time)],
                   ["Base", "Fast Reaction", "Slow Reaction"])
