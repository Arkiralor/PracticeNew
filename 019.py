from json import loads, dumps

file = "html_encoding.txt"
json_file = "html_encodings.json"

with open(file=file, mode="rt", encoding='utf-8')as file_object:
    lines = file_object.readlines()

_dicts = []

for line in lines:
    word_list = line.split("\t")
    letter = word_list[0].strip("\n")
    ascii_enc = word_list[1].strip("\n")
    utf_8 = word_list[2].strip("\n")

    # utf_8.strip("\n")

    data = {
        "letter": letter,
        "ascii": ascii_enc,
        "utf-8": utf_8
    }

    _dicts.append(data)

with open(json_file, mode="w+t", encoding="utf-8")as jfile_obj:
    jdata = dumps(_dicts, indent=4)
    jfile_obj.write(jdata)