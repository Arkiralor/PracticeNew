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
                    "distance": 3.66E+2, ## 3.66 x (10^22) | Megaparsec
                    "velocity": 24.750E+3 ## 24.750 X (10^3) | Kilometres per Hour
                },
                {
                    "distance": 3.66E+2,
                    "velocity": 24.750E+3
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
    resolved = hc * (1/3.08E+19) ## 3.08 * 10^19 kilomentres in a given parsec.
    return (1/resolved)/31_557_600 ## 31,557,600 seconds in a year.

def main():
    ## This is dummy data, replace with your recorded data.
    data = [
                {
                    "distance": 3.66E+2, ## 3.66 x (10^22) | Megaparsec
                    "velocity": 24.750E+3 ## 24.750 X (10^3) | Kilometres per Hour
                },
                {
                    "distance": 3.66E+2,
                    "velocity": 24.750E+3
                }
            ]
    age = calculate_age(hc=calculate_hubble_constant(data=data))

    print(f"The approximate age of the given universe is: {age} years.")

if __name__ == "__main__":
    main()
