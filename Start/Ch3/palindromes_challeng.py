show_expected_result = False
show_hints = False

# first try
def is_palindrome(teststr):
    stringalphas = ""

    for char in teststr:
        if (char.isalpha()):
            stringalphas = stringalphas + char.lower()

    string_midpoint = len(stringalphas) // 2

    first_half = stringalphas[:string_midpoint]
    second_half_reversed = stringalphas[:-string_midpoint - 1:-1]

    return first_half == second_half_reversed

# the most pythonic method
# creates a new string with only alphanumeric characters using built-in string methods
# and checks if it reads the same forwards and backwards

def is_palindrome_clean(s):
    cleaned_s = "".join(char.lower() for char in s if char.isalnum())

    return cleaned_s == cleaned_s[::-1]

# test_word = "Madam, I'm Adam."
# try using some of these other words:
# test_word = "RACE CAR!"
# test_word = "Hello, world"
# test_word = "Radar?"
test_word = "A man, a plan, a canal Panama!"

is_palindrome(test_word)
is_palindrome_clean(test_word)