import sys

for i in range(16):
    try:
        res = 2**(10**i)
        print(f"10^{i}")
        print(sys.getsizeof(res))
        res = None

    except Exception as ex:
        print(f"ERROR at i = {i}: {ex}")