import sys
script, input_encoding, error, file = sys.argv

def main(language_file, encoding, errors):
    line = language_file.readline()

    #check if you reach new line
    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    #print(next_lang)
    print(raw_bytes, "<===>", cooked_string+"\n")


languages = open(file, encoding=input_encoding)

main(languages, input_encoding, error)
