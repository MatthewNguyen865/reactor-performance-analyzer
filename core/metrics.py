import numpy as np

def compute_conversion(CA_in, CA_out):
    """
    Compute reactor conversion.

    Parameters:
        CA_in : inlet concentration array
        CA_out : outlet concentration array

    Returns:
        conversion : conversion array
    """
    
    conversion = (CA_in - CA_out)/CA_in

    return conversion

def compute_reaction_rate(CA_out, time):
    """
    Compute reaction rate using numerical differentiation.

    rA = -dCA/dt

    Parameters:
        CA_out : concentration array
        time : time array

    Returns:
        rate : reaction rate array
    """

    rate = -np.gradient(CA_out, time)
    return rate