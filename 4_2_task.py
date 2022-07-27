def is_palindrome(word):
    """
    Function is_palindrome based on string arguments passed.
    Checks if the characters in the string are the same from left to right as from right to left.
    """
    word1 = word.upper()
    return word1[::-1] == word1

print(is_palindrome('kajak'))
print(is_palindrome('Marcin'))
print(is_palindrome('MalajaLam'))
print(is_palindrome('565'))
print(is_palindrome('712'))
help(is_palindrome)