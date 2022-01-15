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
        print(self._DEC_TO_BINARY)
        print(type(self._DEC_TO_BINARY))

    def check_differences(self) -> int:
        differences: int = 0
        self.convert_to_binary()
        lenght = len(self._BIN_NUM)
        print(lenght)

        try:
            for i in range(lenght-1):
                print(i)
                if self._BIN_NUM[i] == self._DEC_TO_BINARY[i]:
                    differences = differences + 1
            return differences
        except Exception as err:
            return {
                "error": str(err)
            }


def main() -> None:
    numbers = InputClass('121', '11011011')
    print(numbers)
    print(numbers.check_differences())


if __name__ == "__main__":
    main()
