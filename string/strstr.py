"""
Implement strStr().

strstr - locate a substring ( needle ) in a string ( haystack ).
Try not to use standard library string functions for this question.

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

NOTE: Good clarification questions:
What should be the return value if the needle is empty?
What if both haystack and needle are empty?
For the purpose of this problem, assume that the return value should be -1 in both cases.

Solution explanation: Use KMP algorithm

Create largest suffix prefix array
Each index in this array contains the size of the largest possible prefix that is also the suffix for the sub array that
 ends with that index in the original pattern array

"""


# @param A : string
# @param B : string
# @return an integer
def strStr(A, B):
    n, m = len(A), len(B)
    if n == 0 or m == 0:
        return -1
    lsp = [0] * m

    def build_lsp():
        left = 0
        right = 1
        while right < m:
            if B[left] == B[right]:
                lsp[right] = left + 1
                left += 1
                right += 1
            else:
                if left != 0:
                    left = lsp[left - 1]
                else:
                    lsp[right] = 0
                    right += 1

    build_lsp()
    i, j = 0, 0
    while i < n:
        if A[i] == B[j]:
            i += 1
            j += 1

            if j == m:
                return i - m
        else:
            if j != 0:
                j = lsp[j - 1]
            else:
                i += 1
    return -1
