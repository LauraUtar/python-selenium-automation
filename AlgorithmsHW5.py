# Selection Sort
# Implement the selection sort algorithm that is sorting in descending order.
A = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(A)):

    # Find the minimum element in remaining
    # unsorted array
    min_idx = i
    for j in range(i + 1, len(A)):
        if A[min_idx] < A[j]: #to make descending order need to change the sign from > to <
            min_idx = j

    # Swap the found minimum element with
    # the first element
    A[i], A[min_idx] = A[min_idx], A[i]

print(A)



# Bubble Sort
# Implement the bubble sort algorithm that is sorting in descending order.
# O(n^2)
def bubble_sort(arr: list):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
test_list = [5, 4, 7, 9, 1, 6]
print(test_list)
print(bubble_sort(test_list))




# Insertion Sort
# Implement the insertion sort algorithm that is sorting in descending order.
# O(n^2)
def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr

test_list = [6, 4, 2, 5, 1]
print(test_list)
print(insertion_sort(test_list))



# Merge Sort
# Implement the merge sort algorithm that is sorting in descending order.
# O(N * Log N)
def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    return merge_arrays(merge_sort(arr[:middle]), merge_sort(arr[middle:]))
def merge_arrays(left_arr: list, right_arr: list):
    merged_list = []
    i = j = 0
    while i < len(left_arr) or j < len(right_arr):
        if i == len(left_arr):
            merged_list.append(right_arr[j])
            j += 1
            continue
        if j == len(right_arr):
            merged_list.append(left_arr[i])
            i += 1
            continue
        if left_arr[i] >= right_arr[j]:
            merged_list.append(left_arr[i])
            i += 1
        else:
            merged_list.append(right_arr[j])
            j += 1
    return merged_list
test_list = [9, 4, 3, 1, 6, 2, 5]
print(test_list)
print(merge_sort(test_list))