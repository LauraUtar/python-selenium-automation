# Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first. You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

# A Lomuto partition based scheme to
# segregate even and odd numbers.

# function to rearrange the
# array in given way.
def rearrangeEvenAndOdd(arr, n):
    # variables
    j = -1

    # quick sort method
    for i in range(0, n):

        # if array of element
        # is odd then swap
        if (arr[i] % 2 == 0):
            # increment j by one
            j = j + 1

            # swap the element
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp


# Driver code
arr =  [7, 3, 5, 6, 4, 10, 3, 2]
n = len(arr)

rearrangeEvenAndOdd(arr, n)

for i in range(0, n):
    print(arr[i], end=" ")


# Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal integer D and updates the list to represent the integer D + 1.
# For example, if the input is [1, 2, 9] then you should update the array to [1, 3, 0].


def AddOne(digits):
    # initialize an index (digit of units)
    index = len(digits) - 1

    # while the index is valid and the value at [index] ==
    # 9 set it as 0
    while (index >= 0 and digits[index] == 9):
        digits[index] = 0
        index -= 1

    # if index < 0 (if all digits were 9)
    if (index < 0):

        # insert an one at the beginning of the vector
        digits.insert(0, 1)

    # else increment the value at [index]
    else:
        digits[index] += 1


digits = [1, 2, 9]

AddOne(digits)

for digit in digits:
    print(digit, end=' ')