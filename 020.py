"""
Module to first calculate the Hubble Constant using a a list of observations and then derive the age of the universe using H0.
"""

from typing import List
from overloaded_iterables.classes import OverloadedList

def calculate_hubble_constant(data: List[dict] = None)->float:
    """
    Function to calculate the hubble constanct (1/t) based on a dictionary of given distances and values of miscellaneous galaxies from the Earth.

    Arguments:
        data: dict
            index: int
                distance: float
                velocity: float

        Example:
            data = [
                {
                    "distance": 12.3E12, ## 12.3 x (10^12) | Megaparsec
                    "velocity": 3.1E9 ## 3.1 X (10^9) | Kilometres per Hour
                },
                {
                    "distance": 9.3E12,
                    "velocity": 4.1E9
                }
                ...
                etc
            ]

    Returns:
        H0: float | km/s/Mpc
    """
    inverse_time_takens = []
    for item in data:
        inverse_time_takens.append(float(item.get("velocity", 0))/float(item.get("distance", 0)))

    return OverloadedList(inverse_time_takens).mean()

def calculate_age(hc:float=None)->float:
    """
    Function to calculate the age of the universe given a Hubble Constant value.
    """
    return 1/hc

def main():
    ## This is dummy data, replace with your recorded data.
    data = [
                {
                    "distance": 12.3E12, ## 12.3 x (10^12)
                    "velocity": 3.1E3 ## 3.1 X (10^9)
                },
                {
                    "distance": 9.3E12,
                    "velocity": 4.1E2
                }
            ]
    age = calculate_age(hc=calculate_hubble_constant(data=data))

    print(f"The approximate age of the given universe is: {age} years.")

if __name__ == "__main__":
    main()
