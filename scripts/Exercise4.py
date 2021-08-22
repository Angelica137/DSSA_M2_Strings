# Code

def hamming_distance(str1, str2):
    """
    Calculate the hamming distance of the two strings

    Args:
       str1(string),str2(string): Strings to be used for finding the hamming distance
    Returns:
       int: Hamming Distance
    """

    # TODO: Write your solution here
    if len(str1) != len(str2):
        return None
    hamming = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            hamming += 1
    return hamming


# Test Cases
print("Pass" if (9 == hamming_distance('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if (2 == hamming_distance(
    '0101010100011101', '0101010100010001')) else "Fail")
