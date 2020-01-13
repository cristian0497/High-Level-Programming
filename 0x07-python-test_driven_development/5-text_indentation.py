#!/usr/bin/python3
"""
Method - text_indentation
"""


def text_indentation(text):
    """
    Function print a text
    """
    if not isinstance(text, str) or text is None:
        raise TypeError("text must be a string")

    _len = len(text)
    x = 0
    if _len <= 0:
        raise TypeError("text must be a string")
    while x < _len:
        print(text[x], end="")
        if text[x] is '.' or text[x] is '?' or text[x] is ':':
            print('\n')
            try:
                if text[x + 1] == ' ':
                    x += 1
            except:
                pass
        x += 1
