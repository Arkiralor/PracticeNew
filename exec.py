from json import dumps, loads
from subprocess import run

FILE_PATH: str = "output.json"


def open_file():
    try:
        with open(file=FILE_PATH, mode="r+t", encoding="utf-8")as file:
            data = loads(file.read())

        return data
    except Exception as ex:
        print(f"{ex}")
        return None

def write_file(new_data: dict = None):
    data = open_file()
    if data:
        data.append(new_data)
        with open(file=FILE_PATH, mode="w+t", encoding="utf-8")as file:
            writing = dumps(data, indent=4)
            file.write(writing)
        return 0
    
    elif not data:
        with open(file=FILE_PATH, mode="w+t", encoding="utf-8")as file:
            writing = dumps([new_data], indent=4)
            file.write(writing)
        return 1
    
    else:
        return 2

def parse_output(arg: bytes = b""):
    args = arg.decode().split("\n")
    raw_lines = []

    data = {
        "file": None,
        "h0": None,
        "age": None
    }

    for line in args:
        raw_lines.append(line.strip().split(":")[-1].strip())

    data["file"] = raw_lines[0]
    data["h0"] = raw_lines[1]
    data["age"] = raw_lines[2]

    return data
    



def main():
    file_path = "galaxies.json"
    args = ["../HubbleConstant/target/release/hubble-constant.exe", file_path]

    opt = run(args=args, capture_output=True, text=False)
    resp = parse_output(opt.stdout)
    opcode = write_file(new_data=resp)
    print(f"{resp}")

if __name__=='__main__':
    main()