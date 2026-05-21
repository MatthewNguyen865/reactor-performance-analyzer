import pandas as pd

#function to read and extract data
def load_data(filename):
    data = pd.read_csv(filename)

    time = data["Time"]
    CA_in = data["CA_in"]
    CA_out_base = data["CA_out_base"]
    CA_out_fast = data["CA_out_fast"]
    CA_out_slow = data["CA_out_slow"]
    
    return time, CA_in, CA_out_base, CA_out_fast, CA_out_slow
