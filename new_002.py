def main():
    _list = [item for item in range(1, 101)]

    for i in _list:
        if (i % 3 == 0) and (i % 5 != 0):
            print(f"{i} is divisible by 3; FIZZ!")
        elif (i % 5 == 0) and (i % 3 != 0):
            print(f"{i} is divisible by 5; BUZZ!")
        elif (i % 3 == 0) and (i % 5 == 0):
            print(f"{i} is divisible by both 3 and 5; FIZZBUZZ!")
        else:
            print(f"{i}")

        # statement = "Fizz" if ((i % 3 == 0) and (i % 5 != 0)) elif (i % 5 == 0) and (i % 3 != 0) "Buzz" else 


if __name__ == "__main__":
    main()
