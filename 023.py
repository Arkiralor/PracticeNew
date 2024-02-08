"""
Accept two positive integers M and N as input. There are two cases to consider:
(1) If M < N, then print M as output.
(2) If M >= N, subtract N from M. Call the difference M1. 
    If M1 >= N, then subtract N from M1 and call the difference M2. 
    Keep doing this operation until you reach a value k, such that, Mk < N. 
    You have to print the value of Mk as output.
"""


def some_func(m: int, n: int):
    if m <= 0 or n <= 0:
        raise ValueError("Both values need to be positive integers.")
    if m < n:
        print(f"case 1: m = {m}, n = {n}")
        return m
    elif m >= n:
        diff = m - n
        print(
            f"case 2 reached: m = {m}, n = {n}; recursing...or whatever its called...calling `this_func(m={diff}, n={n})`")
        return some_func(diff, n)


def main():
    m, n = 17, 5
    print(some_func(m, n))


if __name__ == "__main__":
    main()
