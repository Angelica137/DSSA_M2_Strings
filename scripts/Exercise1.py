def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # TODO: Write your solution here
    string = ""
    i = len(our_string) - 1
    while i >= 0:
        string += our_string[i]
        i -= 1
        print(string)
    return string
