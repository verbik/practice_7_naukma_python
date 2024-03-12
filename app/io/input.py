import pandas as pd


def input_text_console():
    """
    Input text from the console
    :return: inputted text from the console
    """
    return input("Enter text: ")


def input_text_file(file):
    """
    Read text from the file using build-in python capabilities
    :param file: str, path to the file to read text from
    :return: Read text from the file
    """
    with open(file, 'r') as f:
        return f.read()


def input_text_pandas(file):
    """
    Read text from the file using pandas library
    :param file: str, path to the file to read text from
    :return: The text that was read from the file
    """
    data = pd.read_csv(file)
    return data.to_string()
