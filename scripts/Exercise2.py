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
        return True


# Test Cases
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man',
                                'Notified madman into water') else "Fail")


anagram_checker('lol', 'lolz')
c = 'Dormitory'.split()
d = "".join(c)
print(d)
a = 'Dirty room'.split()
b = "".join(a)
print(b)
