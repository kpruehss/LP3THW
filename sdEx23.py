import sys
script, output_file, input_encoding, error = sys.argv


def main(language_file, encoding, errors, file):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors, file)
        return main(language_file, encoding, errors, file)


def print_line(line, encoding, errors, file):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    file.write(f"{raw_bytes}\n")

    print(raw_bytes, "<===>", cooked_string)


def write_bytes(line, output_file):
    output_file.write(line)


languages = open("languages.txt", encoding="utf-8")
output_file = open(output_file, 'w')

main(languages, input_encoding, error, output_file)

languages.close()
output_file.close()
