import numpy as np
from core.metrics import compute_conversion, compute_reaction_rate
from plotting import plot_conversion, plot_reaction_rate, plot_average_conversion
from core.data_extractor import load_data
from core.comparisons import summarize_scenarios, export_summary_csv
from data_generator import generate_dataset
from core.statistics import percent_improvement, rank_scenarios

#generate and load data
#Note: plots in README.md and data in data.csv use seed = 1
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

conversions = [conversion_base, conversion_fast, conversion_slow]

#compute reaction rates
reaction_rate_base = compute_reaction_rate(CA_out_base, time)
reaction_rate_fast = compute_reaction_rate(CA_out_fast, time)
reaction_rate_slow = compute_reaction_rate(CA_out_slow, time)

reaction_rates = [reaction_rate_base, reaction_rate_fast, reaction_rate_slow]

#plot results
labels = [
    "Base",
    "Fast Reaction",
    "Slow Reaction"
]
all_values = np.concatenate(conversions)
plot_conversion(time,
                np.max(all_values),
                conversions,
                labels)

plot_reaction_rate(time,
                   reaction_rates,
                   labels)

plot_average_conversion(
    labels,
    conversions
)

#summarize results
summarize_scenarios(
    labels,
    conversions,
    reaction_rates
)

export_summary_csv(
    labels,
    conversions,
    reaction_rates
)

#ranking scenarios
ranking = rank_scenarios(labels, conversions)

print("\nScenario Ranking (by Avg Conversion):")
for name, value in ranking:
    print(f"{name}: {value:.3f}")

print("\nPercent Improvement vs Base:")

for i in range(len(labels)):
    if labels[i] != "Base":
        improvement = percent_improvement(conversions[0], conversions[i])
        print(f"{labels[i]}: {improvement:.2f}%")