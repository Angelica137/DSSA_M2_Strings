def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """

    # TODO: Write your solution here
    reverse_str = ""
    for i in range(len(our_string)):
        reverse_str += our_string[len(our_string) - 1 - i]
    return reverse_str

# Test Cases


print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' ==
                 word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' ==
                 word_flipper('This is one small step for ...')) else "Fail")
