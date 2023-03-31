# Below The Arithmetical Mean
# When given a list, the program should return a list of all the elements below the original list’s arithmetical mean.
# The arithmetical mean is the sum of all elements divided by the number of elements.
# Example: [1, 3, 5, 6, 4, 10, 2, 3] (The arithmetical mean is 4.25), Return [1, 3, 4, 2, 3]



def solution(list):
    sum_result = sum(list)
    mean = sum_result / len(list)
    print("Mean:", mean)

    result = []
    for item in list:
        if item < mean:
            result.append(item)

    return result

list = [1, 3, 5, 6, 4, 10, 2, 3]
result = solution(list)
print(result)




# Two Lowest Elements
# When given a list of elements, find the two lowest elements.
# They can be equal to each other or different.
# Example: [198, 3, 4, 9, 10, 9, 2], Return: 2, 3
# [2, 3, 4, 9, 9, 10, 198]

def lowest_element(list):
    list.sort()
    return list[0], list[1]

list = [198, 3, 4, 9, 10, 9, 2]
print(lowest_element(list))
