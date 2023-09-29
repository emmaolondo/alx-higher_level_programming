#!/usr/bin/python3
""" Function that appends a string to a text file """


def append_write(filename="", text=""):
    """A  function that appends a string at the end of
    a text file (UTF8) and returns the number of characters added

    Args:
        filename: The file path or name to be appended to
        text: The information to be added
    Return:
         The number of characters added
    """
    with open(filename, 'a') as file:
        file.write(text)
    file.close()
