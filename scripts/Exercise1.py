def string_reverser(our_string):
    """
    Reverse the input string

    Args:
       our_string(string): String to be reversed
    Returns:
       string: The reversed string
    """

    # TODO: Write your solution here
    string = ""  # O(1)
    i = len(our_string) - 1  # O(1)
    while i >= 0:  # O(n)
        string += our_string[i]  # O(1)
        i -= 1  # O(1)
    return string  # O(1)
