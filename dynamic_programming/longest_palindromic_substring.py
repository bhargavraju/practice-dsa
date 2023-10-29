
"""
Given a string A, find the longest palindromic substring in A. You may assume
that the maximum length of A is 1000. If there are more than one longest
palindromic substrings possible, return the leftmost substring among them.

Input Format
The only argument given is string A.

Output Format
Return the longest palindromic substring in A. If there are more than one
longest palindromic substrings possible, return the leftmost substring among
them.

Constraints
1 <= length( A ) <= 1000
"""


class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        n = len(A)
        is_palindrome = [[False]*n for _ in range(n)]
        # All single char substrings are palindromes
        for i in range(n):
            is_palindrome[i][i] = True
        max_length = 1
        ans = (0, 0)
        # Double char substrings are palindromes if both chars are equal
        for i in range(n-1):
            if A[i] == A[i+1]:
                is_palindrome[i][i+1] = True
                if 2 > max_length:
                    max_length = 2
                    ans = (i, i+1)
        # substrings from index i to j with length greater than 2 are
        # palindromes if i+1 to j-1 is palindrome and string[i] == string[j]
        for i in range(n-3, -1, -1):
            for j in range(i+2, n):
                if is_palindrome[i+1][j-1] and A[i] == A[j]:
                    is_palindrome[i][j] = True
                    if j-i+1 >= max_length:
                        max_length = j-i+1
                        ans = (i, j)
        return A[ans[0]: ans[1]+1]
