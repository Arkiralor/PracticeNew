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
        try:
            self._DEC_NUM = abs(int(int_num))
            self._BIN_NUM = bin_num
        except Exception as err:
            print(
                {
                    "error": str(err)
                }
            )

    def __repr__(self) -> str:
        representation = f"Decimal Number: {self._DEC_NUM}, Binary Number: x0b{self._BIN_NUM}"
        return representation

    def convert_to_binary(self) -> None:
        '''
        Convert the given integer to a binary number with equal number of bits
        to the given binary number.
        '''
        self._DEC_TO_BINARY = bin(self._DEC_NUM).replace("0b", "")
        temp_list = [letter for letter in self._DEC_TO_BINARY]
        try:
            if len(temp_list) < len(self._BIN_NUM) or len(temp_list) == len(self._BIN_NUM):
                additions = len(self._BIN_NUM) - len(temp_list)
                counter = 1
                while (counter <= additions):
                    temp_list.insert(0, '0')
                    counter = counter + 1
                self._DEC_TO_BINARY = ''.join(temp_list)
            elif len(temp_list) > len(self._BIN_NUM):
                print(
                    f"Decimal number '{self._DEC_NUM}' out-of-range of binary number 'x0b{self._BIN_NUM}'."
                    )
                exit()
        except Exception as err:
            print(
                {
                    "error": str(err)
                }
            )

        print(
            f"Decimal number '{self._DEC_NUM}' converted to binary: x0b{self._DEC_TO_BINARY}"
            )

    def check_differences(self) -> int:
        '''
        Check how many bits need to be flipped in the given binary number for it to be
        equivalent to the given positive integer.
        '''
        differences: int = 0
        self.convert_to_binary()
        lenght = len(self._BIN_NUM)

        try:
            for i in range(lenght):
                if self._BIN_NUM[i] != self._DEC_TO_BINARY[i]:
                    differences = differences + 1
            return differences
        except Exception as err:
            return {
                "error": str(err)
            }


def main() -> None:
    '''
    Main function.
    '''
    numbers = InputClass('756', '1111111111')
    print("Numbers: ", numbers)
    print("Binary Digits to flip: ", numbers.check_differences())


if __name__ == "__main__":
    '''
    Driver code.
    '''
    main()
