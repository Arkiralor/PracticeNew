class InputClass:
    _DEC_NUM: int = None
    _BIN_NUM: str = None
    _DEC_TO_BINARY: str = None

    def __init__(self, int_num: str = None, bin_num: str = None) -> None:
        self._DEC_NUM = int(int_num)
        self._BIN_NUM = bin_num

    def __repr__(self) -> str:
        representation = f"Decimal Number: {self._DEC_NUM}, Binary Number: {self._BIN_NUM}"
        return representation

    def convert_to_binary(self) -> None:
        self._DEC_TO_BINARY = bin(self._DEC_NUM).replace("0b", "")
        # print(self._DEC_TO_BINARY)
        # print(type(self._DEC_TO_BINARY))

    def check_differences(self) -> int:
        differences: int = 0
        self.convert_to_binary()
        lenght = len(self._BIN_NUM)-1
        print(lenght)

        for i in range(lenght):
            print(i)
            if self._BIN_NUM[i] == self._DEC_TO_BINARY[i]:
                differences = differences + 1
        return differences

        # for item_1, item_2 in self._DEC_TO_BINARY, self._BIN_NUM:
        #     if item_1 == item_2:
        #         differences = differences + 1
        # return differences


def main() -> None:
    numbers = InputClass('34', '11011011')
    # numbers.convert_to_binary()
    print(numbers.check_differences())


if __name__ == "__main__":
    main()
