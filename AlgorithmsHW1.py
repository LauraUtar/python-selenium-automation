
# Compute the sum of digits in all numbers from 1 to n. When a user enters a number n, find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def compute_sum(n):
    result = 0
    for i in range(n + 1): # 0, 1, 2,3,4,5, 6, 7
        result = result + i
    return result

def compute_sum_2(n):
    return n*(n+1)/2

res = compute_sum(5)
print(res)

res2 = compute_sum_2(5)
print(res2)


# Find max number from 3 values, entered manually from a keyboard.
# Example: 124, 21, 32. Result = 124.

def max_number(a, b, c):
    if a > b and a > c:
        return "a is max number"
    elif b > a and b > c:
        return "b is a max number"
    else:
        return "c is a max number"
print(max_number(4,7,9))


# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: entered number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).

def odd_and_even_numbers(n):
    odd_number = 0
    even_number = 0
    for i in str(n):
        if int(i) % 2 == 0:
            even_number += 1
        else:
            odd_number += 1
    print("Even numbers:", even_number)
    print("Odd numbers:", odd_number)


odd_and_even_numbers(34560)
