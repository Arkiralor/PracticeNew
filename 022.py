"""
In a university, your attendance determines whether you will be allowed to attend your graduation ceremony.
You are not allowed to miss classes for four or more consecutive days.
Your graduation ceremony is on the last day of the academic year, which is the Nth day.

The number of ways to attend classes over N days.
The probability that you will miss your graduation ceremony.
"""

from secrets import choice
from typing import Sequence, List, OrderedDict, Dict
import numpy


def factorial(n: int = 1):
    val = numpy.math.factorial(n)
    return val

class PerCom:
    """
    Class to provide functionality to calculate permutations and Combinations
    """
    n: int = 1
    r: int = 1

    def __init__(self, n:int = 1, r:int = 1):
        if n >= 1:
            self.n = n
        
        if r >= 1:
            self.r = r

        if self.n < self.r:
            raise ValueError("`n` needs to be greater than or equal to `r`.")
        
        print(f"`n` = {self.n}\n`r` = {self.r}")

    def permutation(self):
        
        return factorial(n=self.n)/factorial(n=(self.n - self.r))
    
    def combination(self):
        return factorial(n=self.n)/(
            factorial(self.r)*factorial(
                n=(self.n - self.r)
            )
        )

class Assign:
    days: int = 0
    letters: Sequence[str] = ["A", "B"]

    def __init__(self, days: int = 0):
        if days != 0:
            self.days = days
        self.possible_combination = self.posible_combinations(
            days=self.days, letters=self.letters)

    def posible_combinations(self, letters: Sequence[str], days: int = 0):
        if days == 0:
            return ['']

        result = []
        for letter in letters:
            for combination in self.posible_combinations(days=days - 1, letters=letters):
                result.append(letter + combination)

        return result

    def probability_to_miss_gradution_ceremony(self):
        last_day_absent_count = 0
        valid_combination = 0

        for combination in self.possible_combination:
            if combination.find("AAAA") == -1:
                if combination[-1] == "A":
                    last_day_absent_count += 1
                valid_combination += 1

        print(
            f"The number of ways to attend classes over {self.days} days is {valid_combination}")
        prob: float = last_day_absent_count/valid_combination
        print(
            f"The probability that you will miss your graduation ceremony is {last_day_absent_count}/{valid_combination} i.e, {prob}")


class Attendance:

    VALID_ATTD_MARKS: List[str] = ['A', 'P', 'P',  'P'] ## Let us assume that a student will maintain overall 75% attendance.
    ATTD_DICT: OrderedDict[str, str] = {}
    ATTD_LIST: Sequence[str] = []
    INVALID_ATTD: str = 'AAAA'
    TOTAL_PERMUTATIONS: int = 0

    def __init__(self, attendance_dict: Dict[str, str] = None, *args, **kwargs):
        if attendance_dict:
            self.ATTD_DICT = attendance_dict

        self.ATTD_LIST = [self.ATTD_DICT.get(key) for key in self.ATTD_DICT]
        

    def check_valid_attd(self):
        check = self.INVALID_ATTD in ''.join(self.ATTD_LIST)
        return not check

    @classmethod
    def create_random_attendance(cls, n_days: int = 0, *args, **kwargs):
        attendance_dict = {}
        for i in range(n_days):
            attendance_dict[str(i)] = choice(cls.VALID_ATTD_MARKS)

        return attendance_dict
    
    @classmethod
    def find_n_invalid_attd(cls, n_days: int = 1):
        return PerCom(n=n_days, r=12).permutation()
    
    @classmethod
    def find_n_valid_days(cls, n_days: int =1):
        invalid_days = cls.find_n_invalid_attd(n_days=n_days)
        total_permutations: int = 2**n_days
        return total_permutations - invalid_days
    
    @classmethod
    def find_raw_probability_to_not_graduate(cls, n_days:int=1, n_invalid_days:int=1):
        return n_days/n_invalid_days


        



if __name__ == "__main__":
    # try:
    #     days = int(input("Please enter number of days: "))
    # except ValueError as ex:
    #     print(f"Invalid argument: {ex}")
    # else:
    #     ass = Assign(days=days)
    #     ass.probability_to_miss_graduation_ceremony()

    try:
        days: int = int(input("Enter the number of days the course lasts:\t"))
    except Exception as ex:
        print(f"{ex}")
    # attd_dict = Attendance.create_random_attendance(n_days=days)
    # attd = Attendance(attd_dict)

    n_invalid_days = Attendance.find_n_invalid_attd(n_days=days)
    n_valid_days = Attendance.find_n_valid_days(n_days=days)
    prob_to_not_graduate = Attendance.find_raw_probability_to_not_graduate(n_days=days, n_invalid_days=n_invalid_days)
    prob_to_graduate = 1 - prob_to_not_graduate

    print(f"At random, a student has {prob_to_graduate*100}% chance to graduate with the odds of graduating, based on attendance being {prob_to_not_graduate*100}%.")

    # print(f"The attendance of the student is:\t{attd_dict}")
    # print(f"Attendance List: {attd.ATTD_LIST}")
    # print(
    #     f"The chance that the student will be allowed to graduate is: {attd.check_valid_attd()}")
    # n: int = 90
    # r: int = 2
    # fac = factorial(n)
    # print(f"{n}! = {fac}")
    # percom_obj = PerCom(n=n, r=r)
    # print(f"Permutation for {r} over {n}: {percom_obj.permutation()}")
    # print(f"Combination for {r} over {n}: {percom_obj.combination()}")
