import numpy as np
import pandas as pd

def generate_dataset(filename="data.csv", seed=None):

    rng = np.random.default_rng(seed)

    time = np.array([0, 1, 2, 3, 4, 5])
    CA_in = np.ones_like(time)

    # kinetic parameters
    k_base = rng.uniform(0.2, 0.4)
    k_fast = rng.uniform(0.5, 0.8)
    k_slow = rng.uniform(0.1, 0.2)

    # concentration profiles
    CA_out_base = CA_in * np.exp(-k_base * time)
    CA_out_fast = CA_in * np.exp(-k_fast * time)
    CA_out_slow = CA_in * np.exp(-k_slow * time)

    # measurement noise
    noise = 0.02
    CA_out_base += rng.normal(0, noise, size=len(time))
    CA_out_fast += rng.normal(0, noise, size=len(time))
    CA_out_slow += rng.normal(0, noise, size=len(time))

    df = pd.DataFrame({
        "Time": time,
        "CA_in": CA_in,
        "CA_out_base": CA_out_base,
        "CA_out_fast": CA_out_fast,
        "CA_out_slow": CA_out_slow
    })

    df.to_csv(filename, index=False)

    print(f"Dataset saved to {filename}")