#!/usr/bin/python3
""" function that inserts a line of text to a file, after each line
containing a specific string """


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file, after each line containing
    a specific string

    Args:
        filename : Name of the file
        search_string : The string to be searches
        new_string : the string to insert
    """
    text = ""
    with open(filename) as r:
        for line in r:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as output:
        output.write(text)
