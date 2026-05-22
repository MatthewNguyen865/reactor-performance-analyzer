import numpy as np


def percent_improvement(base, compare):
    """
    Compare scenario against base using average values.
    Positive = improvement
    """
    base_avg = np.mean(base)
    compare_avg = np.mean(compare)

    return ((compare_avg - base_avg) / base_avg) * 100


def rank_scenarios(labels, conversions):
    """
    Rank scenarios by average conversion (descending)
    """
    averages = [np.mean(c) for c in conversions]

    paired = list(zip(labels, averages))
    ranked = sorted(paired, key=lambda x: x[1], reverse=True)

    return ranked

