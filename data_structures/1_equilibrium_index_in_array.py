# Given a sequence arr[] of size n, this function returns
# an equilibrium index (if any) or -1 if no equilibrium index exists.
#
# The equilibrium index of an array is an index such that the sum of
# elements at lower indexes is equal to the sum of elements at higher indexes.
#
#
#
# Example Input:
# arr = [-7, 1, 5, 2, -4, 3, 0]
# Output: 3


def equilibrium_index(arr:list) -> int:
    total_sum = sum(arr)
    left_sum = 0
    for i in range(len(arr)):
        right_sum = total_sum-left_sum-arr[i]
        if right_sum == left_sum:
            return i
        left_sum += arr[i]
    return -1
