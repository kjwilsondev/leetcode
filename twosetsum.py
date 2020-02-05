import os

"""
Sorted Solution
O(nlogn)
"""
def twoSetSum(arr1, arr2, k):
    solutions = []
    # combine both arrays and sort them
    arr1 = sorted(arr1) # O(nlogn)
    arr2 = sorted(arr2) # O(mlogm)
    # left
    l = 0
    # right
    r = len(arr2) - 1
    # code quality: sum
    # best_distance
    # distance
    distance = abs(k - (arr1[l] + arr2[r]))

    while (l <= len(arr1) - 1) and (r >= 0): # O(nm) 
        if abs(k - (arr1[l] + arr2[r])) < distance:
            # delete previous solutions
            solutions = [(arr1[l], arr2[r])]
            distance = abs(k - (arr1[l] + arr2[r]))
        elif abs(k - (arr1[l] + arr2[r])) == distance:
            solutions.append((arr1[l], arr2[r]))
        if (arr1[l] + arr2[r]) < k:
            l += 1
        elif (arr1[l] + arr2[r]) > k:
            r -= 1
        elif (arr1[l] + arr2[r]) == k:
            l, r = l+1, r-1

    return solutions

if __name__ == "__main__":
    # TESTS
    num1 = [9, 13, 1, 8, 12, 4, 0, 5]
    num2 = [3, 17, 4, 14, 6]
    print(twoSetSum(num1, num2, 20)) 
    # [(4, 17), (5, 14), (6, 13)]