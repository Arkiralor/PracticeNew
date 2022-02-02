class HelloWorld:
    _MSG: str = None

    def __init__(self, txt: str = None) -> None:
        self._MSG = txt

    def __repr__(self) -> str:
        return self._MSG

    def show_msg(self) -> None:
        print(self._MSG)


def main() -> None:
    inp = input("Enter the message: ")
    hello_object = HelloWorld(txt=inp)
    hello_object.show_msg()


if __name__ == "__main__":
    main()
