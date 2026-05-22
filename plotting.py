import matplotlib.pyplot as plt
import numpy as np
from config import PLOT_DIR
import os

os.makedirs(PLOT_DIR, exist_ok=True)

def set_plot_style():
    plt.rcParams.update({
        "figure.figsize": (6,4),
        "figure.dpi": 120,

        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,

        "axes.linewidth": 1.1,

        "lines.linewidth": 2,

        "legend.frameon": False,
        "legend.fontsize": 10,

        "grid.alpha": 0.3,

        "xtick.direction": "in",
        "ytick.direction": "in"
    })

def plot_conversion(time, y_upper_lim, conversions, labels):
    set_plot_style()
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

    plt.tight_layout()
    plt.savefig(f"{PLOT_DIR}/conversion_plot.png", dpi=300)

    plt.show()

def plot_reaction_rate(time, rates, labels):
    set_plot_style()
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

    plt.tight_layout()
    plt.savefig(f"{PLOT_DIR}/reaction_rate_plot.png", dpi=300)

    plt.show()

def plot_average_conversion(labels, conversions):
    set_plot_style()

    average_conversions = []

    for conversion in conversions:
        average_conversions.append(np.mean(conversion))

    plt.figure()

    plt.bar(labels, average_conversions)

    plt.ylabel("Average Conversion")
    plt.title("Average Reactor Conversion by Scenario")

    plt.grid(True, axis="y")

    plt.tight_layout()
    plt.savefig(f"{PLOT_DIR}/average_conversion_comparison.png", dpi=300)

    plt.show()