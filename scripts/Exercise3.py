def word_flipper(our_string):
    """
    Flip the individual words in a sentence

    Args:
       our_string(string): String with words to flip
    Returns:
       string: String with words flipped
    """
    # TODO: Write your solution here
    arr = our_string.split()
    for i in range(len(arr)):
        reverse_str = ""
        for j in range(len(arr[i])):
            reverse_str += arr[i][len(arr[i]) - 1 - j]
        arr[i] = reverse_str
    arr = " ".join(arr)
    return arr

# Test Cases


print("Pass" if ('retaw' == word_flipper('water')) else "Fail")
print("Pass" if ('sihT si na elpmaxe' ==
                 word_flipper('This is an example')) else "Fail")
print("Pass" if ('sihT si eno llams pets rof ...' ==
                 word_flipper('This is one small step for ...')) else "Fail")
