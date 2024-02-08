"""
Accept three positive integers as input and check if they form the sides of a right triangle. 
Print YES if they form one, and NO if they do not. 
The input will have three lines, with one integer on each line. The output should be a single line containing one of these two strings: YES or NO.

Hint:
    You just need to check if they are a pythagorean trio i.e., if they satisfy pythagoras' theorem.
"""


def satisfy_pythagoras(a: int = 0, b: int = 0, c: int = 0) -> None:
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError(
            "The sides of any triangle cannot be zero or negative in magnitude.")
    # We sort the three values to find the `proposed` hypotenuse as it will be the longest side.
    side_list = sorted([a, b, c])
    if (side_list[0]**2 + side_list[1]**2) == side_list[2]**2:
        print("YES")
    else:
        print("NO")


def main():
    a = int(input("Enter the first side:\t"))
    b = int(input("Enter the second side:\t"))
    c = int(input("Enter the third side:\t"))

    satisfy_pythagoras(a=a, b=b, c=c)


if __name__ == "__main__":
    main()
