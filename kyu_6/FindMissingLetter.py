import string


# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter
#  in the array. https://www.codewars.com/kata/find-the-missing-letter/train/python
def find_missing_letter(chars):
    current_index = string.ascii_letters.index(chars[0])
    for i in range(1, len(chars)):
        next_index = string.ascii_letters.index(chars[i])
        if current_index == next_index - 1:
            current_index = next_index
        else:
            return list(string.ascii_letters).pop(current_index+1)
    return None
