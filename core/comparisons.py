import numpy as np


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