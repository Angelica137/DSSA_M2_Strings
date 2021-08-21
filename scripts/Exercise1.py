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
    for i in range(len(our_string)):  # O(n)
        string += our_string[len(our_string) - 1 - i]  # O(1)
    return string  # O(1)
