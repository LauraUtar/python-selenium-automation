# Split in Half
# Given a string. Split it into two equal parts. Swap these parts and return the result.
# If the string has odd characters, the first part should be one character greater than the second part.
# Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’.
# string ="aa" "bb">>>>> "bbaa"

def split_string(string):
    length = len(string)
    mid = length // 2 + length % 2 # length = 4 >> 2 + 0 = 2 |||||| length = 5, 2 + 1 = 3
    result = string[mid:] + string[:mid]
    return result

print(split_string("bbbbbcaaaaa"))



# Unique Characters in String
# Given a string, determine if it consists of all unique characters.
# For example, the string 'abcde' has all unique characters and should return True.
# The string 'aabcde' contains duplicate characters and should return False.
#
# def has_unique_char(string):
#     return len(set(string)) == len(string)


def has_unique_char(string):
    char_count = {}
    for char in string:
        if char in char_count:
            return False
        else:
            char_count[char] = 1
    return True



print(has_unique_char('abbcde'))

