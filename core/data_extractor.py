import pandas as pd

#function to read and extract data
def load_data(filename):
    data = pd.read_csv(filename)

    time = data["Time"]
    CA_in = data["CA_in"]
    CA_out = data["CA_out"]

    return time, CA_in, CA_out
