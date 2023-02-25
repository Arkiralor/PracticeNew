'''
Python script to find the largest number from a set of DIGITS included in
an alphanumeric string.

Eg:
    Input: I have 3 whole crates; enough to feed 7 people for 2 whole months.
    Output: 732
'''
from typing import List

class InputString:
    input_string: str=None
    digit_list: List[str] = []

    def __init__(self, input_string):
        self.input_string = input_string
    
    def __repr__(self):
        rep = f"Input String: {self.input_string}"
        return rep

    def find_digits(self) -> None:
        self.digit_list = [character for character in self.input_string if character.isdigit()]
        print(f"Digits Found: {self.digit_list}")
    
    def find_largest_number(self) -> int:
        self.find_digits()
        largest_list = sorted(self.digit_list, reverse=True)
        largest_number = ''.join(largest_list)
        return int(largest_number)

def main() -> None:
    entry = input("\nPlease enter a candidate string: ")
    input_string = InputString(entry)
    print(f"Input: {input_string}")

    op = input_string.find_largest_number()
    print(f"\nLargest Number Possible: {op}")


if __name__ == "__main__":
    main()