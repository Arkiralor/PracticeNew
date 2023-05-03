from os import path
import numpy as np
from secrets import choice

from overloaded_iterables.classes import OverloadedList, OverloadedSet, Queue, Stack

def main():
    arr = [choice([i for i in range(1, 5)]) for _ in range(1, 10) ]

    _list = OverloadedList(arr)
    _set = OverloadedSet(arr)

    ## Display
    print("\n")
    print(f"List:\t{_list}")
    print(f"Set:\t{_set}")
    print("\n")

    ## Arithmetic Mean
    print("\n")
    print(f"Arithmetic Mean (list):\t{_list.mean()}")
    print(f"Arithmetic Mean (set):\t{_set.mean()}")
    print("\n")

    ## Sorting
    print("\n")
    print(f"Sorting (list):\t{_list.sort()}")
    print(f"Sorting (list, reversed):\t{_list.sort(reverse=True)}")
    print("\n")
    print(f"Sorting (set):\t{_set.sort()}")
    print(f"Sorting (set, reversed):\t{_set.sort(reverse=True)}")
    print("\n")

    ## Raise each element to a given power 'e'
    power = choice([i for i in np.arange(-3, 3.5, 0.5)])
    print("\n")
    print(f"'e' = {power}")
    print(f"Raised (list):\t{_list.raise_to(power=power)}")
    print(f"Raised (set):\t{_set.raise_to(power=power)}")
    print("\n")

    ## Root-Mean-Square
    print("\n")
    print(f"RMS (list):\t{_list.rms()}")
    print(f"RMS (Set):\t{_set.rms()}")
    print("\n")

    ## Median
    print("\n")
    print(f"Median (list):\t{_list.median()}")
    print(f"Median (set):\t{_set.median()}")
    print("\n")

    ## Length
    print("\n")
    print(f"Length (list):\t{_list.len}")
    print(f"Length (set):\t{_set.len}")
    print("\n")

    ## Frequencies (OverloadedList only) returns [values][frequencies]
    print("\n")
    values, frequencies = _list.frequencies
    print(f"Values:\t\t{values}")
    print(f"Frequencies:\t{frequencies}")
    print(f"Zipped:\t\t{OverloadedList(zip(values, frequencies))}")
    print("\n")

    ## Histogram
    # save_dir = path.dirname(__file__)
    # print("\n")
    # _list.hist(bins=_list.len,show=True, save_dir=save_dir, file_name='new')
    # print("\n")

    ## Queue and Stack
    arr = ["a", "b", "c", "d", "e"]
    queue = Queue(arr)
    stack = Stack(arr)

    print("\n")
    print(f"Queue (original):\t{queue}")
    print(f"Stack (original):\t{stack}")
    print("\n")

    args_ = OverloadedList({"f", "g", "h"})
    queue.insert(args_)
    stack.insert(args_)

    print(f"Queue (inserted {args_}):\t{queue}")
    print(f"Stack (inserted {args_}):\t{stack}")

    _pop = choice([i for i in range(1, 5)])
    queue.pop(_pop)
    stack.pop(_pop)

    print(f"Queue (popped {_pop}):\t{queue}")
    print(f"Stack (popped {_pop}):\t{stack}")


if __name__=="__main__":
    main()