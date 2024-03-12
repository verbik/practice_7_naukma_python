def output_text_console(text):
    """
    Outputs text to console
    :param text: str, the text to be outputted to the console
    :return: None
    """
    print(text)


def output_text_file(text, file):
    """
    Write text to a file
    :param text: str, the text to be written to the file
    :param file: str, the path to the file
    :return: None
    """
    with open(file, 'w') as f:
        f.write(text)
