import statistics as st
import random as rand

def create_list(size:int):
    rand.seed()

    gen_list = [rand.randint(1,1_000_000_000) for _ in range(size)]
    return gen_list

def main():
    size = int(input("Please enter the size of the list: "))
    gen_list = create_list(size)
    gen_list = sorted(gen_list, reverse=False)
    # print(f"Generated List: {gen_list}")
    print(f"The mean of the list is: {st.fmean(gen_list)}")
    print(f"The mode of the list is: {st.mode(gen_list)}")
    print(f"The median of the list is: {st.median(gen_list)}")

if __name__=="__main__":
    main()