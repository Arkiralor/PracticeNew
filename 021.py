"""
Module to first calculate the Hubble Constant using a a list of observations and then derive the age of the universe using H0.

Store the observational data in `galaxies.json` found in the directory.
"""
from json import loads
from typing import List
from overloaded_iterables.classes import OverloadedList
from pydantic import BaseModel

## Or you can also use a class instead of the dict.
class GalaxyModel(BaseModel):
    name: str
    distance: float
    velocity: float

    @property
    def h0(self) -> float:
        return float(self.velocity/self.distance)


def calculate_h0(data: List[GalaxyModel] = None) -> float:
    """
    Function to calculate the mean Hubble's Constant

    It is defined as the helioradical velocity divided by the distance from Earth FOR VERY FAR AWAY GALAXIES.
    """
    data = OverloadedList([item.h0 for item in data])
    h0 = data.mean()
    print(f"Hubble's Constant calculated:\t{h0}km/s/Mpc")
    return h0


def calculate_age(h0: float = None, unit: str = "years") -> float:
    """
    Find the age of the universe in `unit`.

    `unit`: years | seconds

    Link: https://www.e-education.psu.edu/astro801/content/l10_p5.html
    """
    # 3.08 * 10^19 kilomentres in a given parsec.
    resolved = resolved = h0 * (1/3.08E+19)  

    if unit.lower().strip() == "years":
        return (1/resolved)/31.5576E+6  # 31.5576 * 10^6 seconds in a year.
    elif unit.lower().strip() == "seconds":
        return 1/resolved
    else:
        raise ValueError(
            f"Invalid unit `{unit}`; correct options are: 'years' | 'seconds'.")


def read_data(file_path: str = "galaxies.json") -> List[GalaxyModel]:
    if not file_path:
        raise ValueError(f"File: {file_path} not found.")

    with open(file=file_path, mode="rt", encoding="utf-8") as file_obj:
        data = loads(file_obj.read())

    results = []

    for item in data:
        obj = GalaxyModel(**item)
        results.append(obj)

    return results


def main():
    ## This is dummy data, replace with your recorded data in `galaxies.json`
    data = read_data("galaxies.json")
    age = calculate_age(h0=calculate_h0(data=data), unit="years")

    print(f"The approximate age of the given universe is: {age} years.")


if __name__ == "__main__":
    main()
