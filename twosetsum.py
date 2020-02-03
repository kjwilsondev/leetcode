import os

"""
Sorted Solution
O(nlogn)
"""
def twoSetSum(arr1, arr2, k):
    solutions = []
    # combine both arrays and sort them
    arr = sorted(arr1 + arr2) # O(nlogn)
    # left
    l = 0
    # right
    r = len(arr) - 1
    distance = abs(k - (arr[l] + arr[r]))
    print(arr)

    while l < r:
        print(arr[l], arr[r])
        if abs(k - (arr[l] + arr[r])) < distance:
            # delete previous solutions
            print("reset")
            solutions = [(arr[l], arr[r])]
            # l, r = l+1, r-1
        elif abs(k - (arr[l] + arr[r])) == distance:
            solutions.append((arr[l], arr[r]))
            l, r = l+1, r-1
        if (arr[l] + arr[r]) < k:
            l += 1
        elif (arr[l] + arr[r]) > k:
            r -= 1
        print(f"s: {solutions}")

    return solutions

if __name__ == "__main__":
    # TESTS
    num1 = [9, 13, 1, 8, 12, 4, 0, 5]
    num2 = [3, 17, 4, 14, 6]
    print(twoSetSum(num1, num2, 20)) 
    # [(4, 17), (5, 14), (6, 13)]