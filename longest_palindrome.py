import os

"""
Longest Palindromic SubString
"""

"""
Nested for loop solution
O(n^3)
"""


def longestPalindrome(s):
    solution = None
    solution_length = 0

    for i in range(0, len(s)):  # O(n)
        print(f"Left at index {i}")
        for j in range(1, len(s)):  # O(n)
            print(f"Right at index {j}")
            print(s[i:j])
            if s[i:j] == s[i:j][::-1]:  # O(n-(n...0)) => O(n)
                if len(s[i:j]) >= solution_length:
                    solution = s[i:j]
                    solution_length = len(s[i:j])
    return solution


if __name__ == "__main__":
    # TESTS
    print(longestPalindrome("abacdcdefedaba"))
