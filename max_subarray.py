# Given an array of integers, find maximum length subarray having given sum.

# For example,
# Arr = [5,6,-5,5,3,5,3,-2,0]
# sum = 8

# Output:
# [-5,5,3,5]

# Two loops
def two_loops(arr, num):
    # instantiate old solution is []
    final_solution = []
    # iterate through array with index i
    for i in range(0, len(arr)):
        # iterate through array with index i2 starting at i
        for i2 in range(0, len(arr)):
            current_solution = []
            # if indexes are the same, just look at one without adding
            if i == i2:
                if arr[i] == num:
                    current_solution = [arr[i]]
            # else if indexes are different
            else:
                # sum the range between i and i2
                current_solution = arr[i:i2+1]
                print(f"current solution: {current_solution}")
            # if sum matches our num
            if sum(current_solution) == num:
                # if len(solution) is bigger than len(old solution)
                if len(current_solution) > len(final_solution):
                    (f"new final: {current_solution}")
                    final_solution = current_solution
    return final_solution

arr = [5,6,-5,5,3,5,3,-2,0]
num = 8
print(two_loops(arr, num))