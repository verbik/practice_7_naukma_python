from app.io.input import *
from app.io.output import output_text_console, output_text_file


def main():
    text_from_console = input_text_console()
    print(text_from_console)

    text_from_file = input_text_file("./data/read_file.txt")
    print(text_from_file)

    text_from_pandas = input_text_pandas("./data/read_file.txt")
    print(text_from_pandas)

    output_text_console("Output text to console")

    output_text_file("Output text to file", "./data/write_file.txt")


if __name__ == "__main__":
    main()
