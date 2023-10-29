"""
Given a string A of size N.
Return the string A after reversing the string word by word.

NOTE:
A sequence of non-space characters constitutes a word.
Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
If there are multiple spaces between words, reduce them to a single space in the reversed string.

Problem Constraints
1 <= N <= 3 * 10^5

Example
Input: "the sky is blue"
Output: "blue is sky the"
"""


# @param A : string
# @return a strings
def solve(A):
    words = A.split()
    left, right = 0, len(words) - 1
    while left <= right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1
    return " ".join(words)
