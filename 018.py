from datetime import datetime
from os import path
import numpy as np
from secrets import choice

from overloaded_iterables.classes import OverloadedList, OverloadedSet, Queue, Stack

def main():
    ts1 = datetime.utcnow().timestamp()
    arr = [choice([i for i in range(1, 5)]) for _ in range(1, 10) ]
    ts2 = datetime.utcnow().timestamp()
    ## Display
    print("\n")
    print(f"This took:\t{ts2-ts1} sec")
    print("\n")

    ts3 = datetime.utcnow().timestamp()
    _list = OverloadedList(arr)
    _set = OverloadedSet(arr)
    ts4 = datetime.utcnow().timestamp()

    ## Display
    print("\n")
    print(f"List:\t{_list}")
    print(f"Set:\t{_set}")
    print(f"This took:\t{ts4-ts3} sec")
    print("\n")

    ## Arithmetic Mean
    print("\n")
    ts5 = datetime.utcnow().timestamp()
    print(f"Arithmetic Mean (list):\t{_list.mean()}")
    print(f"Arithmetic Mean (set):\t{_set.mean()}")
    ts6 = datetime.utcnow().timestamp()
    print(f"This took:\t{ts6-ts5} sec")
    print("\n")

    ## Sorting
    print("\n")
    ts7 = datetime.utcnow().timestamp()
    print(f"Sorting (list):\t{_list.sort()}")
    print(f"Sorting (list, reversed):\t{_list.sort(reverse=True)}")
    ts8 = datetime.utcnow().timestamp()
    print(f"This took:\t{ts8-ts7} sec")
    print("\n")
    ts9 = datetime.utcnow().timestamp()
    print(f"Sorting (set):\t{_set.sort()}")
    print(f"Sorting (set, reversed):\t{_set.sort(reverse=True)}")
    ts10 = datetime.utcnow().timestamp()
    print("\n")

    ## Raise each element to a given power 'e'
    ts11 = datetime.utcnow().timestamp()
    power = choice([i for i in np.arange(-3, 3.5, 0.5)])
    ts12 = datetime.utcnow().timestamp()
    print("\n")
    print(f"'e' = {power}")
    ts13 = datetime.utcnow().timestamp()
    print(f"Raised (list):\t{_list.raise_to(power=power)}")
    print(f"Raised (set):\t{_set.raise_to(power=power)}")
    ts14 = datetime.utcnow().timestamp()
    print("\n")

    ## Root-Mean-Square
    print("\n")
    ts15 = datetime.utcnow().timestamp()
    print(f"RMS (list):\t{_list.rms()}")
    print(f"RMS (Set):\t{_set.rms()}")
    ts16 = datetime.utcnow().timestamp()
    print("\n")

    ## Median
    print("\n")
    ts17 = datetime.utcnow().timestamp()
    print(f"Median (list):\t{_list.median()}")
    print(f"Median (set):\t{_set.median()}")
    ts18 = datetime.utcnow().timestamp()
    print("\n")

    ## Length
    print("\n")
    ts19 = datetime.utcnow().timestamp()
    print(f"Length (list):\t{_list.len}")
    print(f"Length (set):\t{_set.len}")
    ts20 = datetime.utcnow().timestamp()
    print("\n")

    ## Frequencies (OverloadedList only) returns [values][frequencies]
    print("\n")
    ts21 = datetime.utcnow().timestamp()
    values, frequencies = _list.frequencies
    ts22 = datetime.utcnow().timestamp()
    print(f"Values:\t\t{values}")
    print(f"Frequencies:\t{frequencies}")
    print(f"Zipped:\t\t{OverloadedList(zip(values, frequencies))}")
    print("\n")

    ## Histogram
    # save_dir = path.dirname(__file__)
    # print("\n")
    # _list.hist(bins=_list.len,show=True, save_dir=save_dir, file_name='new')
    # print("\n")

    ## Queue and 
    ts23 = datetime.utcnow().timestamp()
    arr = ["a", "b", "c", "d", "e"]
    queue = Queue(arr)
    stack = Stack(arr)
    ts24 = datetime.utcnow().timestamp()

    print("\n")
    ts25 = datetime.utcnow().timestamp()
    print(f"Queue (original):\t{queue}")
    print(f"Stack (original):\t{stack}")
    ts26 = datetime.utcnow().timestamp()
    print("\n")

    ts27 = datetime.utcnow().timestamp()
    args_ = OverloadedList({"f", "g", "h"})
    ts28 = datetime.utcnow().timestamp()
    ts29 = datetime.utcnow().timestamp()
    queue.insert(args_)
    stack.insert(args_)
    ts30 = datetime.utcnow().timestamp()

    print(f"Queue (inserted {args_}):\t{queue}")
    print(f"Stack (inserted {args_}):\t{stack}")

    ts31 = datetime.utcnow().timestamp()
    _pop = choice([i for i in range(1, 5)])
    ts32 = datetime.utcnow().timestamp()
    ts33 = datetime.utcnow().timestamp()
    queue.pop(_pop)
    stack.pop(_pop)
    ts34 = datetime.utcnow().timestamp()

    print(f"Queue (popped {_pop}):\t{queue}")
    print(f"Stack (popped {_pop}):\t{stack}")


if __name__=="__main__":
    main()