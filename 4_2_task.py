def is_palindrome(word):
    """
    Function is_palindrome based on string arguments passed.
    Checks if the characters in the string are the same from left to right as from right to left.
    """
    if word.upper()[::-1] == word.upper():
        return True
    else:
        return False

print(is_palindrome('kajak'))
print(is_palindrome('Marcin'))
print(is_palindrome('MalajaLam'))
print(is_palindrome('565'))
print(is_palindrome('712'))
help(is_palindrome)