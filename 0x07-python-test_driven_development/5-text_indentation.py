#!/usr/bin/python3
""" text_indentation module """


def text_indentation(text):
    """ a function that prints a text with 2 new lines 
    after each of these characters: ., ? and :.

    Args:
       text: string text.

    Raises:
        TypeError: if text not string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    new_text = ""

    text_line = len(text)

    for i in range(text_line):
        if text[i] == ' ':
            if new_text == "" or new_text[-1] == "\n":
                continue
            new_text += text[i]
        elif text[i] in punctuation:
            new_text += text[i] + "\n\n"
        else:
            new_text += text[i]
    print(new_text, end="")
