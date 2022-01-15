'''
Python script to check how many bits would need to be flipped in a given binary number for it to be equivalent
to a given, positive integer (whole number).
'''
class InputClass:
    '''
    Class to compare a given binary number and a given positive integer.
    '''
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
        new_list = []
        for item in self._DEC_TO_BINARY:
            new_list.append(item)
        try:
            if len(new_list) < len(self._BIN_NUM):
                additions = len(self._BIN_NUM) - len(new_list)
                counter = 1
                while (counter <= additions):
                    new_list.insert(0, '0')
                    counter = counter + 1
                self._DEC_TO_BINARY = ''.join(new_list)
            elif len(new_list) > len(self._BIN_NUM):
                print(
                    f"Decimal number '{self._DEC_NUM}' out-of-range of binary number '{self._BIN_NUM}'.")
                exit()
        except Exception as err:
            print(
                {
                    "error": str(err)
                }
            )

        print(
            f"Decimal number '{self._DEC_NUM}' converted to binary: ", self._DEC_TO_BINARY)

    def check_differences(self) -> int:
        differences: int = 0
        self.convert_to_binary()
        lenght = len(self._BIN_NUM)

        try:
            for i in range(lenght-1):
                if self._BIN_NUM[i] != self._DEC_TO_BINARY[i]:
                    differences = differences + 1
            return differences
        except Exception as err:
            return {
                "error": str(err)
            }


def main() -> None:
    numbers = InputClass('0', '110110110')
    print("Numbers: ", numbers)
    print("Binary Digits to change: ", numbers.check_differences())


if __name__ == "__main__":
    main()
