import sys

def text_analyzer(text=None):
    """

    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.
    """
    if text is None:
        text = input("What is the text to analyze?\n")
    elif not isinstance(text, str):
        print("AssertionError: argument is not a string")
        return None
    upper = 0
    lower = 0
    punctuation = 0
    space = 0
    for i in text:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i in ".,;:!?\"'()[]{}-":
            punctuation += 1
        elif i.isspace():
            space += 1
    print("The text contains ", len(text), " character(s):")
    print("-", upper, "upper letter(s)")
    print("-", lower, "lower letter(s)")
    print("-", punctuation, "punctuation mark(s)")
    print("-", space, "space(s)")

if __name__=="__main__":
    if len(sys.argv) != 2:
        print("error message")
    else:
        text_analyzer(sys.argv[1])
