"""
Given two binary strings, return their sum (also a binary string).

Example:
a = "100"
b = "11"
Return a + b = "111".
"""


# @param A : string
# @param B : string
# @return a strings
def addBinary(A, B):
    n, m = len(A), len(B)
    carry = 0
    i, j = n - 1, m - 1
    ans = ""
    while i >= 0 or j >= 0:
        s = 0
        s += int(A[i]) if i >= 0 else 0
        s += int(B[j]) if j >= 0 else 0
        s += carry
        elem = s % 2
        carry = s // 2
        ans = str(elem) + ans
        i -= 1
        j -= 1

    if carry > 0:
        ans = "1" + ans

    return ans
