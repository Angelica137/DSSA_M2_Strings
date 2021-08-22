# Code

def anagram_checker(str1, str2):
    """
    Check if the input strings are anagrams of each other

    Args:
       str1(string),str2(string): Strings to be checked
    Returns:
       bool: Indicates whether strings are anagrams
    """

    # TODO: Write your solution here
    str1_split = str1.split()
    str1_join = "".join(str1_split)
    str2_split = str2.split()
    str2_join = "".join(str2_split)
    if len(str1_join) != len(str2_join):
        return False
    else:
        str1_arr = sorted(str1_join.lower())
        print(str1_arr)

        str2_arr = sorted(str2_join.lower())
        print(str2_arr)
        if str1_arr == str2_arr:
            return True
