"""
Groot has a profound love for palindrome which is why he keeps fooling around with strings.
A palindrome string is one that reads the same backward as well as forward.

Given a string A of size N consisting of lowercase alphabets, he wants to know if it is possible to make the
given string a palindrome by changing exactly one of its character.

Example Input
Input 1:
 A = "abbba"
Input 2:
 A = "adaddb"

Example Output
Output 1:
 "YES"
Output 2:
 "NO"
"""


# @param A : string
# @return a strings
def solve(A):
    n = len(A)
    i, j = 0, n - 1
    mismatch_count = 0
    while i <= j:
        if A[i] != A[j]:
            mismatch_count += 1
        i += 1
        j -= 1

    if mismatch_count == 1 or (mismatch_count == 0 and n % 2 == 1):
        return "YES"
    return "NO"
