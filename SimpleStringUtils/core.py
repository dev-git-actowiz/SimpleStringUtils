# SimpleStringUtils/core.py

def count_vowels(input_string):
    """
    Count the number of vowels in a given string.
    :param input_string: str, the string to check
    :return: int, count of vowels
    """
    vowels = "aeiouAEIOU"
    return sum(1 for char in input_string if char in vowels)
