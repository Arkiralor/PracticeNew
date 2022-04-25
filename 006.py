import pandas as pd
from sympy import isprime
from time import time

def find_prime_numbers(limit):
    t1 = time()
    ds = pd.Series(range(2,limit+1))
    ds = ds[ds.apply(isprime)].tolist()
    t2 = time()
    return ds, t2-t1

def main():
    limit = 100_000
    ds, t = find_prime_numbers(limit)
    print(f'Prime numbers found: {len(ds)}')
    print(ds)
    print(f'Time taken: {t}')

if __name__ == '__main__':
    main()