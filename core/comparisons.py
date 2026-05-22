import numpy as np
import pandas as pd


def average_conversion(conversion):
    return np.mean(conversion)


def peak_conversion(conversion):
    return np.max(conversion)


def average_reaction_rate(rate):
    return np.mean(rate)


def peak_reaction_rate(rate):
    return np.max(rate)


def summarize_scenarios(
        labels,
        conversions,
        reaction_rates):

    print("\nReactor Performance Summary")
    print("-" * 40)

    for i in range(len(labels)):

        avg_conv = average_conversion(conversions[i])
        peak_conv = peak_conversion(conversions[i])

        avg_rate = average_reaction_rate(reaction_rates[i])
        peak_rate = peak_reaction_rate(reaction_rates[i])

        print(f"\nScenario: {labels[i]}")
        print(f"Average Conversion: {avg_conv:.3f}")
        print(f"Peak Conversion: {peak_conv:.3f}")
        print(f"Average Reaction Rate: {avg_rate:.3f}")
        print(f"Peak Reaction Rate: {peak_rate:.3f}")

def export_summary_csv(
        labels,
        conversions,
        reaction_rates,
        filename="output/reactor_summary.csv"):

    summary_data = []

    for i in range(len(labels)):

        scenario_data = {
            "Scenario": labels[i],

            "Average Conversion":
                np.mean(conversions[i]),

            "Peak Conversion":
                np.max(conversions[i]),

            "Average Reaction Rate":
                np.mean(reaction_rates[i]),

            "Peak Reaction Rate":
                np.max(reaction_rates[i])
        }

        summary_data.append(scenario_data)

    summary_df = pd.DataFrame(summary_data)

    summary_df.to_csv(filename, index=False)

    print(f"Summary exported to {filename}")