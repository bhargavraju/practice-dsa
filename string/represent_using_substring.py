"""
Given a String consisting of lowercase English alphabets A, Find if the given string can be represented from a
substring by iterating the substring two or more times.
"""


# @param A : string
# @return an integer
def solve(A):
    n = len(A)
    appended = A + A
    left = 1
    while left < n:
        if A == appended[left:left + n]:
            return 1
        left += 1
    return 0
