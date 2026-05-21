import matplotlib.pyplot as plt
import numpy as np

def plot_conversion(time, y_upper_lim, conversions, labels):
    """
    time: array of time values
    conversions: list of conversion arrays
    labels: list of names for each curve
    """

    for i in range(len(conversions)):
        plt.plot(time, conversions[i], label=labels[i])

    plt.ylabel("Conversion")
    plt.xlabel("Time")
    plt.title("Reactor Conversion Over Time")
    plt.legend()
    plt.ylim(0, y_upper_lim)
    plt.grid(True)

    plt.savefig("example_plots/conversion_plot.png", dpi=300)

    plt.show()

def plot_reaction_rate(time, rates, labels):
    """
    time: array of time values
    rates: list of reaction rate arrays
    labels: list of names for each curve
    """

    for i in range(len(rates)):
        plt.plot(time, rates[i], label=labels[i])

    plt.ylabel("Reaction Rate")
    plt.xlabel("Time")
    plt.title("Reaction Rate Over Time")
    plt.legend()
    plt.grid(True)

    plt.savefig("example_plots/reaction_rate_plot.png", dpi=300)

    plt.show()