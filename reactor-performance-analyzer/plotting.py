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

    plt.show()
