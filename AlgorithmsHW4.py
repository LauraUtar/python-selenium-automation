# Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]

# A Lomuto partition based scheme to
# segregate even and odd numbers.

# function to rearrange the
# array in given way.
def rearrangeEvenAndOdd(arr, n):
    # variables
    j = -1 #for the position before the first one

    # quick sort method
    for i in range(0, n):

        # if array of element
        # is odd then swap
        if (arr[i] % 2 == 0):
            # increment j by one
            j = j + 1

            # swap the element
            # arr[i], arr[j] = arr[j], arr[i]
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp


# Driver code
arr = [7, 3, 5, 6, 4, 10, 3, 2]
n = len(arr)

rearrangeEvenAndOdd(arr, n)

for i in range(0, n):
    print(arr[i], end=" ")


# Increment a Number
# Write a program that takes as input a list of digits encoding a nonnegative decimal
# integer D and updates the list to represent the integer D + 1.
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

#Solution 2:
def solution_2(digits):
    # convert the array of int into an array of str
    str_arr = [str(i) for i in digits]

    # convert the array of str into a str. For example ['1', '2', '3'] -> '123'
    str_digits = ''.join(str_arr)

    # Increase the value of the number inside the string
    str_digits =  str(int(str_digits) + 1)

    # convert and return the str into an array of numbers. For example ['1', '2', '3'] -> [1, 2, 3]
    return [int(i) for i in str_digits]

print("\nresult with solution 2:", solution_2([1, 2, 9]))




# Even First
# Your input is a list of integers, and you have to reorder its entries so that the even entries appear first.
# You are required to solve it without allocating additional storage (operate with the input list).
# Example: [7, 3, 5, 6, 4, 10, 3, 2] Return [6, 4, 10, 2, 7, 3, 5, 3]
def even_odd_sort(arr):
    # start two index, one at the beginning of the list and another one in the final position
    left = 0
    right = len(arr) - 1

    while left < right:
        # We are going to repeat this process until the left index is lesser than the right index

        # We will move the left index until it reaches an even number
        while arr[left] % 2 == 0 and left < right:
            left += 1

        # We will move the right index until it reaches an odd number
        while arr[right] % 2 != 0 and left < right:
            right -= 1

        # Swap the numbers at the left and right index
        arr[left], arr[right] = arr[right], arr[left]

    return arr


arr = [1, 2, 3, 5, 4, 9]
print(even_odd_sort(arr))  # Output: [4, 2, 3, 5, 1, 9]