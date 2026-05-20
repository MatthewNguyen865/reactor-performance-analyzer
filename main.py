import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from plotting import plot_conversion
from data_extractor import load_data

#load data
time, CA_in, CA_out = load_data("data.csv")

#compute conversion, reactor performance
#baseline
conversion_base = (CA_in - CA_out)/CA_in

#faster reaction (simulate by decreasing CA_out)
CA_out_fast = CA_out * 0.8
conversion_fast = (CA_in - CA_out_fast)/CA_in

#slower reaction (simulate by increasing CA_out)
CA_out_slow = CA_out * 1.2
conversion_slow = (CA_in - CA_out_slow)/CA_in

#plot results
all_values = np.concatenate([conversion_base, conversion_fast, conversion_slow])
plot_conversion(time,
                max(all_values),
                [conversion_base, conversion_fast, conversion_slow],
                ["Base", "Fast Reaction", "Slow Reaction"])
