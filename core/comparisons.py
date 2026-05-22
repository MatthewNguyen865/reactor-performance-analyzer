import numpy as np
import pandas as pd
from config import OUTPUT_DIR
import os

def ensure_output_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

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

    for label, conversion, rate in zip(labels, conversions, reaction_rates):

        avg_conv = average_conversion(conversion)
        peak_conv = peak_conversion(conversion)

        avg_rate = average_reaction_rate(rate)
        peak_rate = peak_reaction_rate(rate)

        print(f"\nScenario: {label}")
        print(f"Average Conversion: {avg_conv:.3f}")
        print(f"Peak Conversion: {peak_conv:.3f}")
        print(f"Average Reaction Rate: {avg_rate:.3f}")
        print(f"Peak Reaction Rate: {peak_rate:.3f}")

def export_summary_csv(
        labels,
        conversions,
        reaction_rates,
        filename=f"{OUTPUT_DIR}/reactor_summary.csv"):

    summary_data = []

    for label, conversion, rate in zip(labels, conversions, reaction_rates):

        scenario_data = {
            "Scenario": label,

            "Average Conversion":
                np.mean(conversion),

            "Peak Conversion":
                np.max(conversion),

            "Average Reaction Rate":
                np.mean(rate),

            "Peak Reaction Rate":
                np.max(rate)
        }

        summary_data.append(scenario_data)

    summary_df = pd.DataFrame(summary_data)

    ensure_output_dir()
    summary_df.to_csv(filename, index=False)

    print(f"Summary exported to {filename}")