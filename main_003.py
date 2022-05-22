import statistics as st
import random as rand
from sympy import isprime
import pandas as pd
import matplotlib.pyplot as plt

def create_list(size:int):
    rand.seed()

    gen_list = [rand.randint(1,1_000_000_000) for _ in range(size)]
    return gen_list

def generate_df(size):
    stat_list = []
    for i in range(1000):
        gen_list = create_list(size)
        # print(f"Generated List: {gen_list}")
        # print(f"The mean of the list is: {st.fmean(gen_list)}")
        # print(f"The mode of the list is: {st.mode(gen_list)}")
        # print(f"The median of the list is: {st.median(gen_list)}")
        mean_ = st.fmean(gen_list)
        median_ = st.mode(gen_list)
        mode_ = st.mode(gen_list)
        iteration_ = i
        stat_dict = {
            "iteration": iteration_+1,
            "mean": mean_,
            "median": median_,
            "mode": mode_,
        }
        stat_list.append(stat_dict)

    df = pd.DataFrame(stat_list)
    # print(df.head(5))
    return df

def main():
    size = int(input("Please enter the size of the list: "))
    df = generate_df(size)
    p1=plt.plot(df["iteration"], df["mean"], label="mean", color="red")
    p2=plt.plot(df["iteration"], df["median"], label="median", color="blue")
    p3=plt.plot(df["iteration"], df["mode"], label="mode", color="green")
    plt.legend()
    plt.show()

    gen_list = create_list(size)
    plt.hist(gen_list, 100)
    plt.show()
if __name__=="__main__":
    main()